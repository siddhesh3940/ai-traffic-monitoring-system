#!/usr/bin/env python3
"""
Traffic Monitoring System Startup Script
Run this script to start the traffic monitoring application.
"""

import sys
import subprocess
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def check_files():
    """Check if required files exist"""
    required_files = [
        "app3.py",
        "requirements.txt",
        "templates/index.html",
        "templates/traffic_light.html",
        "templates/dqn_graphs.html"
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files found")
    return True

def start_server():
    """Start the FastAPI server"""
    print("🚀 Starting Traffic Monitoring System...")
    print("📍 Server will be available at: http://localhost:8000")
    print("🔄 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "app3.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

def main():
    """Main function"""
    print("🚦 Traffic Monitoring System")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Check required files
    if not check_files():
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Start server
    start_server()

if __name__ == "__main__":
    main()