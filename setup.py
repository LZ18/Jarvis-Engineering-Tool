#!/usr/bin/env python3
"""
Setup script for Jarvis Engineering Diagnostic System
"""

import os
import sys
import subprocess
import shutil

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def setup_environment():
    """Set up environment file"""
    env_file = ".env"
    example_file = "env_example.txt"
    
    if os.path.exists(env_file):
        print("✅ .env file already exists")
        return True
    
    if os.path.exists(example_file):
        try:
            shutil.copy(example_file, env_file)
            print("✅ Created .env file from template")
            print("⚠️  Please edit .env file and add your OpenAI API key")
            return True
        except Exception as e:
            print(f"❌ Failed to create .env file: {e}")
            return False
    else:
        print("❌ env_example.txt not found")
        return False

def check_ffmpeg():
    """Check if FFmpeg is available"""
    ffmpeg_path = os.path.join("ffmpeg-2025-06-11-git-f019dd69f0-essentials_build", "bin", "ffmpeg.exe")
    if os.path.exists(ffmpeg_path):
        print("✅ FFmpeg found in project directory")
        return True
    else:
        print("⚠️  FFmpeg not found in project directory")
        print("   The system will try to use system-installed FFmpeg")
        return True

def main():
    """Main setup function"""
    print("🚀 Setting up Jarvis Engineering Diagnostic System")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install dependencies
    if not install_dependencies():
        return False
    
    # Setup environment
    if not setup_environment():
        return False
    
    # Check FFmpeg
    check_ffmpeg()
    
    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit .env file and add your OpenAI API key")
    print("2. Run: python main.py")
    print("\n🔗 Get your API key from: https://platform.openai.com/api-keys")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
