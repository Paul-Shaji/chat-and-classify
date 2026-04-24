# --- Import necessary libraries ---
import streamlit as st
from PIL import Image
import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2, preprocess_input, decode_predictions
)
import os, google.generativeai as genai
from dotenv import load_dotenv

# --- Load environment variables from .env file (for API key) ---
load_dotenv()

# --- Streamlit page configuration ---
st.set_page_config(page_title="AI Multi-App", page_icon="🤖", layout="wide")

# --- Sidebar navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "AI Image Classifier", "Gemini Chatbot"])

# ===========================
# --------- HOME ------------
# ===========================
if page == "Home":
    st.title("🤖 Welcome to AI Multi-App")
    st.write(
        """
        - 🖼 AI Image Classifier → Upload an image and classify it.
        - 🤖 Gemini Chatbot → Chat with a Gemini AI assistant.
        """
    )
    st.info("👉 Use the sidebar to switch between apps.")

# ===========================
# ---- IMAGE CLASSIFIER -----
# ===========================
elif page == "AI Image Classifier":
    st.title("🖼 AI Image Classifier")

    # Load the MobileNetV2 model only once and cache it
    @st.cache_resource
    def load_model():
        return MobileNetV2(weights="imagenet")

    # Preprocess uploaded image for model prediction
    def preprocess_image(image):
        img = np.array(image)
        img = cv2.resize(img, (224, 224))  # Resize to MobileNetV2 input size
        img = preprocess_input(img)        # Normalize pixels
        img = np.expand_dims(img, axis=0)  # Add batch dimension
        return img

    # Get predictions from the model
    def classify_image(model, image):
        processed = preprocess_image(image)
        preds = model.predict(processed)
        return decode_predictions(preds, top=3)[0]  # Return top-3 predictions

    model = load_model()
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        if st.button("Classify"):
            with st.spinner("Analyzing..."):
                image = Image.open(uploaded_file)
                preds = classify_image(model, image)
                st.subheader("Predictions")
                for _, label, score in preds:
                    st.write(f"{label} ({score:.2%})")  # Display label and confidence

# ===========================
# -------- CHATBOT ----------
# ===========================
elif page == "Gemini Chatbot":
    st.title("🤖 Gemini Chatbot")

    # Configure the Gemini API key
    try:
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    except Exception as e:
        st.error(f"⚠ API Key Error: {str(e)}. Please set your GOOGLE_API_KEY in the .env file.")
        st.stop()
        
    st.caption("💡 Gemini API is free up to certain limits. Check usage on [Google AI Studio](https://aistudio.google.com/app/apikey).")

    # Initialize chat session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input box
    if prompt := st.chat_input("Ask me anything..."):
        # Save user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        try:
            # Send prompt to Gemini API with streaming response
            with st.chat_message("assistant"):
                placeholder = st.empty()
                full_response = ""
                
                model = genai.GenerativeModel('gemini-2.5-flash')

                
                # Streaming is handled by iterating over the response
                for chunk in model.generate_content(prompt, stream=True):
                    full_response += chunk.text
                    placeholder.markdown(full_response + "▌")  # "typing" effect

                placeholder.markdown(full_response)

            # Save assistant response
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response}
            )

        # Handle any exceptions from the API call
        except Exception as e:
            st.error(f"⚠ Gemini API error: {str(e)}")







#   # .\venv\Scripts\activate 
#   #  .\venv\Scripts\python.exe -m streamlit run app.py