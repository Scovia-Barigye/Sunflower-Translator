# Sunflower: Uganda Connect 🌻

**The All-in-One Local Uganda AI Hub**

A Streamlit web application powered by **Sunbird AI** that seamlessly translates English into several Ugandan languages (Luganda, Runyankole, Ateso, Luo, Lugbara, Lusoga). The app supports multi-modal inputs including text, document uploads, and even features native in-browser voice recording and playback!

## Features
- 📝 **English-to-Local Text Translation**: Translate raw English text directly to native Ugandan languages flawlessly. 
- 📄 **Document Extraction & Smart Chunking**: Upload `.txt`, `.pdf`, or `.docx` files. The app extracts the text and automatically truncates overly large documents to safely bypass TTS synthesis character-limits (max 10,000 characters).
- 🎤 **Voice Translation & Audio Waves**: Natively record your voice from the browser, or upload `.mp3`/`.wav` files. The UI features **Gemini-style pulsing audio wave animations** when recognizing the voice. It uses Sunbird's Speech-to-Text (STT) API to transcribe the audio into English before translation.
- 🎧 **Audio Playback**: Automatically generates spoken audio of the translated local language phrases utilizing Sunbird's Text-to-Speech (TTS) API so you can listen to the translation immediately.
- 🎨 **Beautiful Animated UI**: Modern, tailor-made UI featuring **Glowing CSS Title Animations**, Tailwind CSS styling, FontAwesome icons, outfit fonts, and a vibrant theme.
- ⚡ **Optimized Architecture**: Avoids slow LLM (Large Language Model) routing by specifically executing via Sunbird's raw NMT (Neural Machine Translation) endpoint directly, resulting in up to 10x faster translations!

## Prerequisites
- Python 3.8+
- A developer API key from [Sunbird AI](https://sunbird.ai).

## Installation

1. **Clone the repository** (or download the files):
   ```bash
   git clone <your-repo-url>
   cd Sunflower-Translator
   ```

2. **Create a Virtual Environment** (Recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: This project requires `streamlit>=1.39.0` to support the native `st.audio_input` widget, and `pypdf` / `python-docx` for document parsing).*

## Running the Application

Once your virtual environment is active and dependencies are installed, you can start the application by running:

```bash
streamlit run app.py
```

The app will compile and automatically open in your default web browser (usually accessible at `http://localhost:8501`).

## How to use the App

1. Launch the app and look at the sidebar on the left.
2. Under **Hub Settings**, securely enter your **Sunbird API Key**.
3. In the main window, choose your preferred method of input:
   - **TEXT Tab**: Type standard text.
   - **FILE UPLOAD Tab**: Upload a document to have its contents extracted.
   - **AUDIO / VOICE Tab**: Click the microphone to record your voice or upload an audio file.
4. Select your desired **Target Language** from the dropdown menu. (Source is locked to English for guaranteed accuracy).
5. Hit **Translate Now**.
6. **Results**: The app will display your original English text beside the local translation. Click play on the generated audio player attached to listen to the pronunciation!

## Reviewing and Contributing

If you wish to review, use, or contribute to this code:
- **Fork the repository** to make your own changes.
- **Found an issue or have a feature idea?** Feel free to open an Issue or submit a Pull Request.
- **Code Structure**: The core layout logic, Tailwind/CSS animations, multi-modal input processing, and Sunbird API payload handlers are contained within `app.py`. Audio animations map to `wave_animation.py`. 

## License

This project is made available for educational and open-source purposes. Feel free to adapt and expand on it!
