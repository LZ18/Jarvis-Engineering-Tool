import whisper
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile
from dotenv import load_dotenv
from openai import OpenAI
import os
import asyncio
import edge_tts
from playsound import playsound
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from ultralytics import YOLO
import base64
import io
from engineering_vision import EngineeringVisionAnalyzer

# === Load .env and OpenAI API ===
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# === Load Whisper model once ===
print("⏳ Loading Whisper model...")
model = whisper.load_model("base")

# === Initialize Engineering Vision Analyzer ===
print("⏳ Initializing Engineering Vision Analyzer...")
vision_analyzer = EngineeringVisionAnalyzer()

# === Video Analysis Functions ===
def capture_video_frame(camera_index=0, duration=3):
    """Capture a video frame from webcam"""
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("❌ Could not open camera")
        return None
    
    print("📹 Capturing video frame...")
    frames = []
    start_time = cv2.getTickCount()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        frames.append(frame)
        cv2.imshow('Jarvis Video Analysis', frame)
        
        # Capture for specified duration
        if (cv2.getTickCount() - start_time) / cv2.getTickFrequency() > duration:
            break
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    if frames:
        return frames[-1]  # Return the last frame
    return None

def analyze_engineering_components(frame):
    """Analyze engineering components in the frame using enhanced vision analyzer"""
    # Use the enhanced vision analyzer
    detections = vision_analyzer.detect_components(frame)
    wiring_analysis = vision_analyzer.analyze_wiring_patterns(frame)
    color_detections = vision_analyzer.detect_color_components(frame)
    
    # Create comprehensive analysis report
    analysis_report = vision_analyzer.create_analysis_report(
        frame, detections, wiring_analysis, color_detections
    )
    
    return analysis_report

def encode_image_to_base64(image):
    """Convert PIL image to base64 string"""
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

def create_analysis_prompt(frame, user_query="", analysis_report=None):
    """Create a detailed prompt for engineering analysis using enhanced vision analyzer"""
    return vision_analyzer.create_enhanced_prompt(frame, user_query, analysis_report)

# === Edge TTS function using playsound ===
async def speak(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        mp3_path = temp_audio.name

    communicate = edge_tts.Communicate(text=text, voice="en-GB-RyanNeural")
    await communicate.save(mp3_path)

    playsound(mp3_path)

# === Main conversation loop ===
async def main():
    messages = [
        {"role": "system", "content": """You are Jarvis, an expert engineering diagnostic assistant with computer vision capabilities. 
You can analyze video feeds of engineering projects like breadboards, circuits, and mechanical assemblies. 
You provide detailed technical analysis, identify wiring errors, component issues, and suggest improvements.
You speak like a knowledgeable engineer - technical but approachable, using humor when appropriate."""}
    ]

    while True:
        try:
            print("\n🎙️ Jarvis Engineering Diagnostic System")
            print("Options:")
            print("1. 📹 Analyze video feed (press 'v')")
            print("2. 🎤 Voice analysis (press 's')")
            print("3. 👋 Exit (say 'goodbye Jarvis')")
            
            choice = input("\nChoose option (v/s/voice): ").lower().strip()
            
            if choice == 'v' or choice == 'video':
                # Video analysis mode
                print("📹 Starting video analysis...")
                frame = capture_video_frame()
                
                if frame is not None:
                    print("🔍 Analyzing engineering components...")
                    
                    # Get user query for analysis
                    user_query = input("What specific aspect should I analyze? (or press Enter for general analysis): ")
                    
                    # Perform comprehensive analysis
                    analysis_report = analyze_engineering_components(frame)
                    print(f"📊 Analysis Summary: {analysis_report['total_components']} components detected")
                    
                    # Create analysis prompt with enhanced data
                    prompt, base64_image = create_analysis_prompt(frame, user_query, analysis_report)
                    
                    # Add user message with image
                    messages.append({
                        "role": "user", 
                        "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                        ]
                    })
                    
                    # Generate GPT-4 Vision response
                    print("🤖 Analyzing with computer vision...")
                    response = client.chat.completions.create(
                        model="gpt-4-vision-preview",
                        messages=messages,
                        max_tokens=500,
                        temperature=0.7
                    )
                    
                    jarvis_reply = response.choices[0].message.content.strip()
                    print("🔧 Engineering Analysis:")
                    print(jarvis_reply)
                    
                    # Add assistant message
                    messages.append({"role": "assistant", "content": jarvis_reply})
                    
                    # Speak the analysis
                    await speak(jarvis_reply)
                    
                else:
                    print("❌ Failed to capture video frame")
                    
            elif choice == 's' or choice == 'voice' or choice == '':
                # Voice analysis mode (original functionality)
                print("\n🎙️ Jarvis is listening. Say 'goodbye Jarvis' to end the conversation.")
                print("🎤 Listening... Speak now.")

                # === Record voice ===
                DURATION = 5
                SAMPLERATE = 44100
                audio = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1)
                sd.wait()

                # === Transcribe ===
                with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                    wav.write(f.name, SAMPLERATE, audio)
                    result = model.transcribe(f.name)

                transcript = result["text"].strip()
                print("🧠 You said:", transcript)

                # === Exit condition ===
                if "goodbye jarvis" in transcript.lower():
                    print("👋 Exiting Jarvis.")
                    await speak("Goodbye, Jarvis.")
                    return

                # === Add user message ===
                messages.append({"role": "user", "content": transcript})

                # === Generate GPT response ===
                print("🤖 Thinking...")
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=300
                )

                jarvis_reply = response.choices[0].message.content.strip()
                print("🗣️ Jarvis says:", jarvis_reply)

                # === Add assistant message and speak ===
                messages.append({"role": "assistant", "content": jarvis_reply})
                await speak(jarvis_reply)

        except Exception as e:
            print(f"⚠️ Error: {e}")
            return

# === Run the loop ===
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Jarvis interrupted manually.")
