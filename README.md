AI Multi-App: Chat & Classify

A powerful Streamlit application that combines AI-powered image classification with an intelligent chatbot interface. This multi-functional app leverages state-of-the-art machine learning models to provide two distinct AI experiences in one seamless interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

### 🖼️ AI Image Classifier
- Upload images in JPG, JPEG, or PNG format
- Powered by **MobileNetV2** pre-trained on ImageNet
- Returns top-3 predictions with confidence scores
- Real-time image processing with optimized preprocessing
- Supports 1000+ object categories

### 💬 Gemini Chatbot
- Interactive conversational AI powered by **Google's Gemini 2.5 Flash**
- Streaming responses for a natural chat experience
- Persistent chat history during your session
- Free tier available with generous API limits
- Real-time "typing" effect for engaging UX

## 📋 Prerequisites

- Python 3.8 or higher
- Google API Key (for Gemini Chatbot feature)
- Virtual environment (recommended)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Paul-Shaji/chat-and-classify.git
cd chat-and-classify
```

### 2. Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install streamlit
pip install pillow
pip install opencv-python
pip install tensorflow
pip install numpy
pip install google-generativeai
pip install python-dotenv
```

Or create a `requirements.txt` file with:
```
streamlit
pillow
opencv-python
tensorflow
numpy
google-generativeai
python-dotenv
```

Then install with:
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

**To get your Google API Key:**
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create or select a project
3. Generate an API key
4. Copy and paste it into your `.env` file

## 🎯 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Using the Image Classifier

1. Navigate to **AI Image Classifier** from the sidebar
2. Click **"Browse files"** to upload an image
3. Select an image (JPG, JPEG, or PNG)
4. Click the **"Classify"** button
5. View the top-3 predictions with confidence scores

### Using the Gemini Chatbot

1. Navigate to **Gemini Chatbot** from the sidebar
2. Type your message in the chat input at the bottom
3. Press Enter or click Send
4. The AI will respond with streaming text
5. Chat history is maintained throughout your session

## 🏗️ Project Structure

```
chat-and-classify/
│
├── app.py                 # Main Streamlit application
├── .env                   # Environment variables (API keys)
├── .gitignore            # Git ignore file
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 🔑 Key Technologies

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Web framework for the UI |
| **TensorFlow/Keras** | Deep learning framework for image classification |
| **MobileNetV2** | Pre-trained CNN model for image recognition |
| **Google Gemini API** | Large language model for chatbot functionality |
| **OpenCV** | Image preprocessing |
| **PIL (Pillow)** | Image handling |

## 🎨 Features Breakdown

### Image Classification Pipeline

1. **Image Upload**: User uploads an image through Streamlit's file uploader
2. **Preprocessing**: Image is resized to 224x224 pixels and normalized
3. **Prediction**: MobileNetV2 model processes the image
4. **Results**: Top-3 predictions with confidence percentages

### Chatbot Architecture

1. **Input Processing**: User message captured via Streamlit chat input
2. **API Request**: Message sent to Gemini 2.5 Flash API
3. **Streaming Response**: Real-time streaming of AI response
4. **State Management**: Chat history stored in Streamlit session state

## 🔐 Security Notes

- Never commit your `.env` file to version control
- The `.gitignore` file should include `.env`
- Keep your Google API key confidential
- Monitor your API usage on Google AI Studio

## 📊 API Usage Limits

Google Gemini API offers a generous free tier:
- Monitor your usage at [Google AI Studio](https://aistudio.google.com/app/apikey)
- Check current rate limits and quotas
- Consider implementing rate limiting for production use

## 🐛 Troubleshooting

### Common Issues

**1. API Key Error:**
```
⚠ API Key Error: Please set your GOOGLE_API_KEY in the .env file.
```
**Solution:** Ensure your `.env` file exists and contains a valid Google API key

**2. Model Loading Issues:**
```
Error loading MobileNetV2 model
```
**Solution:** Ensure TensorFlow is properly installed. Try reinstalling:
```bash
pip uninstall tensorflow
pip install tensorflow
```

**3. Module Not Found:**
```
ModuleNotFoundError: No module named 'streamlit'
```
**Solution:** Activate your virtual environment and install dependencies

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Add your `GOOGLE_API_KEY` in Secrets management
5. Deploy!

### Deploy to Other Platforms

The app can also be deployed to:
- Heroku
- Google Cloud Run
- AWS Elastic Beanstalk
- Azure App Service

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Add support for custom model training
- [ ] Implement user authentication
- [ ] Add database for chat history persistence
- [ ] Support for multiple image uploads
- [ ] Export chat conversations
- [ ] Add more AI models for classification
- [ ] Implement image-to-image generation
- [ ] Add voice input/output for chatbot

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Paul Shaji**
- GitHub: [@Paul-Shaji](https://github.com/Paul-Shaji)

## 🙏 Acknowledgments

- [Google AI](https://ai.google.dev/) for Gemini API
- [TensorFlow](https://www.tensorflow.org/) for MobileNetV2
- [Streamlit](https://streamlit.io/) for the amazing framework
- ImageNet dataset for pre-trained models

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the [Streamlit Documentation](https://docs.streamlit.io/)
- Review [Google AI Documentation](https://ai.google.dev/docs)

---

<div align="center">
Made with ❤️ and Python | Star ⭐ this repository if you found it helpful!
</div>
