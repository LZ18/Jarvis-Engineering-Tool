<<<<<<< HEAD
# Jarvis Engineering Diagnostic System

An advanced AI-powered engineering diagnostic assistant that combines computer vision, voice recognition, and natural language processing to analyze engineering projects in real-time.

## 🚀 Features

### 🔍 Computer Vision Analysis
- **Real-time video analysis** of engineering projects
- **Component detection** using YOLO object detection
- **Wiring pattern analysis** for identifying connection errors
- **Color-based component recognition** (resistors, capacitors, ICs)
- **Breadboard connection verification**
- **Error detection** for common wiring mistakes

### 🎤 Voice Interface
- **Speech-to-text** using OpenAI Whisper
- **Text-to-speech** using Microsoft Edge TTS
- **Natural conversation** with engineering expertise
- **Voice commands** for system control

### 🤖 AI-Powered Analysis
- **GPT-4 Vision** for detailed image analysis
- **Engineering-specific prompts** for technical feedback
- **Actionable recommendations** for fixing issues
- **Component identification** and verification

## 📋 Requirements

### Hardware
- Webcam or camera for video analysis
- Microphone for voice input
- Speakers for audio output

### Software Dependencies
- Python 3.8+
- FFmpeg (included in project)
- All Python packages listed in `requirements.txt`

## 🛠️ Installation

### Option 1: Clone from GitHub
```bash
git clone https://github.com/yourusername/jarvis-engineering-diagnostic.git
cd jarvis-engineering-diagnostic
```

### Option 2: Download and Extract
Download the project files and extract to your desired location.

### Setup Steps

#### Quick Setup (Recommended)
```bash
python setup.py
```

#### Manual Setup
1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   - Copy `env_example.txt` to `.env`
   - Edit `.env` and add your OpenAI API key:
   ```bash
   cp env_example.txt .env
   # Then edit .env and replace 'your_openai_api_key_here' with your actual API key
   ```

3. **Get your OpenAI API key:**
   - Visit: https://platform.openai.com/api-keys
   - Create a new API key
   - Add it to your `.env` file

4. **Ensure FFmpeg is accessible** (included in project)

## 🎯 Usage

### Starting the System
```bash
python main.py
```

### Available Options

1. **📹 Video Analysis Mode**
   - Press `v` or type `video`
   - Captures video feed from webcam
   - Analyzes engineering components
   - Provides detailed technical feedback
   - Speaks the analysis results

2. **🎤 Voice Analysis Mode**
   - Press `s` or type `voice`
   - Records voice input
   - Processes speech through Whisper
   - Generates AI responses
   - Speaks the response

3. **👋 Exit**
   - Say "goodbye Jarvis" or use Ctrl+C

## 🔧 Engineering Analysis Capabilities

### Component Detection
- **Resistors, capacitors, ICs**
- **Wires and connections**
- **Breadboard components**
- **LEDs and other electronic parts**

### Error Detection
- **Wrong pin connections** (e.g., A4 instead of A3)
- **Loose or missing wires**
- **Incorrect component orientation**
- **Short circuit risks**
- **Open circuit issues**

### Analysis Features
- **Wiring pattern analysis**
- **Color-based component identification**
- **Connection verification**
- **Component count and type detection**
- **Potential issue identification**

## 📁 Project Structure

```
Jarvis/
├── main.py                    # Main application file
├── engineering_vision.py      # Computer vision analysis module
├── test_openai.py            # OpenAI API test file
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── .env                     # Environment variables (create this)
├── venv/                    # Virtual environment
└── ffmpeg-2025-06-11-git-f019dd69f0-essentials_build/  # FFmpeg binaries
```

## 🎨 Example Use Cases

### Breadboard Analysis
1. Point camera at breadboard
2. Select video analysis mode
3. Ask: "Check if my LED circuit is wired correctly"
4. Jarvis will identify components and verify connections

### Circuit Debugging
1. Show circuit to camera
2. Ask: "Why isn't my circuit working?"
3. Jarvis will analyze wiring and identify potential issues

### Component Verification
1. Display components to camera
2. Ask: "Are these resistors the correct values?"
3. Jarvis will identify components and verify specifications

## 🔍 Technical Details

### Computer Vision Pipeline
1. **Frame Capture** - Real-time video from webcam
2. **Component Detection** - YOLO model identifies objects
3. **Wiring Analysis** - Edge detection and line analysis
4. **Color Detection** - HSV-based component recognition
5. **Report Generation** - Comprehensive analysis summary
6. **AI Analysis** - GPT-4 Vision provides detailed feedback

### Voice Processing Pipeline
1. **Audio Recording** - 5-second voice capture
2. **Speech Recognition** - OpenAI Whisper transcription
3. **AI Processing** - GPT-3.5-turbo response generation
4. **Text-to-Speech** - Edge TTS audio output

## 🚨 Troubleshooting

### Common Issues

1. **Camera not working**
   - Check camera permissions
   - Ensure camera is not in use by other applications

2. **Audio issues**
   - Verify microphone permissions
   - Check audio device settings

3. **FFmpeg errors**
   - Ensure FFmpeg is in PATH
   - Check FFmpeg installation

4. **OpenAI API errors**
   - Verify API key in .env file
   - Check API quota and billing

### Performance Tips
- Use good lighting for video analysis
- Keep camera steady during capture
- Speak clearly for voice recognition
- Ensure stable internet connection for AI processing

## 🔮 Future Enhancements

- **Custom YOLO model** trained on engineering components
- **Circuit simulation** integration
- **3D component recognition**
- **Multi-camera support**
- **Real-time streaming analysis**
- **Component database integration**

## 📄 License

This project is for educational and personal use. Please respect OpenAI's terms of service and usage policies.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the system.

## 📦 GitHub Setup

### Creating a Repository
1. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Name it: `jarvis-engineering-diagnostic`
   - Make it public or private
   - Don't initialize with README (we already have one)

2. **Initialize and push your local repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Jarvis Engineering Diagnostic System"
   git branch -M main
   git remote add origin https://github.com/yourusername/jarvis-engineering-diagnostic.git
   git push -u origin main
   ```

### Security Notes
- ✅ `.env` file is automatically ignored (contains your API key)
- ✅ `venv/` folder is ignored (virtual environment)
- ✅ `__pycache__/` folders are ignored
- ✅ Temporary files are ignored

### For Contributors
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Commit: `git commit -m 'Add feature'`
5. Push: `git push origin feature-name`
6. Submit a pull request

---

**Jarvis Engineering Diagnostic System** - Your AI-powered engineering assistant! 🔧🤖
=======
# Jarvis-Engineering-Tool
Jarvis is a AI Automated tool that takes voice and video feedback and gives you solutions to issues like wiring, voltage and mounting problems. It can run a diagnostic on a video and tell you where your issue lies. 
>>>>>>> fee9de3240402e6c0caae1f070a5ffd63261d5a1
