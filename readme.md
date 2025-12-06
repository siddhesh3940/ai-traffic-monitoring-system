# Traffic Monitoring System with AI

A comprehensive traffic monitoring and management system using computer vision, reinforcement learning, and intelligent traffic light control.

## 📸 Screenshots

### Main Dashboard
![Main Dashboard](screenshot/Screenshot%202025-12-06%20173936.png)

### Video Upload Interface
![Video Upload](screenshot/Screenshot%202025-12-06%20173949.png)

### Live Traffic Monitoring
![Live Monitoring](screenshot/Screenshot%202025-12-06%20174004.png)

### Traffic Light Simulation
![Traffic Light Simulation](screenshot/Screenshot%202025-12-06%20174045.png)

### DQN Analytics Dashboard
![DQN Analytics](screenshot/Screenshot%202025-12-06%20174053.png)

## 🚀 Features

- **Real-time Vehicle Detection**: Uses YOLO (You Only Look Once) for accurate vehicle detection and classification
- **Multi-directional Monitoring**: Simultaneous monitoring of traffic from 4 directions (North, South, East, West)
- **Vehicle Classification**: Detects cars, trucks, buses, motorcycles, and bicycles
- **Reinforcement Learning**: Deep Q-Network (DQN) agent for intelligent traffic light optimization
- **Web Dashboard**: Real-time analytics and visualization
- **Traffic Light Simulation**: Adaptive traffic signal control based on traffic density

## 📋 Requirements

- **Python 3.8 or higher**
- **Windows/Linux/macOS**
- **Webcam or video files** for traffic monitoring

## 🛠️ Installation & Setup

### Method 1: Quick Demo (Fastest - Recommended for Testing)

**Try the system with auto-generated demo videos:**

```bash
python auto_demo.py
```

This will automatically:
- ✅ Generate 4 demo traffic videos
- ✅ Start the web server
- ✅ Upload videos and start processing
- ✅ Open ready-to-use dashboard

**OR use the interactive demo setup:**

```bash
python demo_setup.py
```

Provides step-by-step guidance and generates demo data.

📖 **See [DEMO_GUIDE.md](DEMO_GUIDE.md) for detailed demo instructions**

### Method 2: Quick Start

1. **Clone or download** this project to your computer
2. **Open terminal/command prompt** in the project directory
3. **Run the startup script**:
   ```bash
   python run.py
   ```

The script will automatically:
- Check Python version compatibility
- Install required dependencies
- Start the web server

### Method 3: Manual Installation

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**:
   ```bash
   python app3.py
   ```

## 🌐 Usage

### Quick Demo (No Video Upload Needed)

If you used `auto_demo.py`, the system is already running with demo videos!

1. **Open browser**: `http://localhost:8000`
2. **View Live Monitoring**: See vehicles being detected in real-time
3. **Try Traffic Light Simulation**: Click the button to see AI optimization

### Manual Usage

1. **Access the web interface**: Open your browser and go to `http://localhost:8000`

2. **Upload Videos**: 
   - Go to the "Upload Videos" tab
   - Upload traffic videos for each direction (MP4, AVI, MOV formats)
   - **OR use demo videos** from `uploads/` folder:
     - `demo_right.mp4` → Right/East direction
     - `demo_down.mp4` → Down/South direction  
     - `demo_left.mp4` → Left/West direction
     - `demo_up.mp4` → Up/North direction
   - Configure Region of Interest (ROI) for each direction
   - Click "Upload & Process All Videos"

3. **Monitor Traffic**:
   - Switch to "Live Monitoring" tab
   - View real-time vehicle counts and processed video feeds
   - Monitor traffic statistics and analytics

4. **Traffic Light Simulation**:
   - Navigate to `/traffic_light` or click "Traffic Light Simulation"
   - Start the intelligent traffic light control system
   - View DQN analytics at `/dqn_analytics`

## 📊 Key Components

### 1. Video Processing (`app3.py`)
- FastAPI web server
- OpenCV for video processing
- YOLO model for object detection
- Real-time frame processing and analysis

### 2. Reinforcement Learning
- **Q-Learning Agent**: Basic reinforcement learning for traffic optimization
- **Deep Q-Network (DQN)**: Advanced neural network-based learning
- **Adaptive Traffic Control**: Dynamic signal timing based on traffic density

### 3. Web Interface
- **Dashboard**: Real-time monitoring and analytics
- **Video Upload**: Easy video file management
- **Traffic Simulation**: Interactive traffic light control
- **Analytics**: Performance metrics and learning progress

## 🎯 How It Works

1. **Video Analysis**: The system processes uploaded traffic videos using computer vision
2. **Vehicle Detection**: YOLO model identifies and classifies vehicles in real-time
3. **Traffic Counting**: Vehicles are counted within defined regions of interest
4. **AI Decision Making**: DQN agent learns optimal traffic light timing patterns
5. **Adaptive Control**: Traffic lights adjust timing based on current traffic density
6. **Performance Monitoring**: System tracks efficiency and learning progress

## 📁 Project Structure

```
backend/
├── app3.py                 # Main FastAPI application
├── run.py                  # Startup script
├── auto_demo.py            # Automated demo with auto-upload
├── demo_setup.py           # Interactive demo setup
├── generate_demo_data.py   # Demo video generator
├── requirements.txt        # Python dependencies
├── README.md               # Main documentation
├── DEMO_GUIDE.md           # Demo usage guide
├── templates/              # HTML templates
│   ├── index.html         # Main dashboard
│   ├── traffic_light.html # Traffic simulation
│   └── dqn_graphs.html    # Analytics dashboard
├── static/                # CSS and static files
├── uploads/               # Uploaded video files (demo videos here)
├── images/                # Processed images
└── yolov8n.pt             # YOLO model (auto-downloaded)
```

## 🔧 Configuration

### Region of Interest (ROI)
- Configure detection areas for each direction
- Values are relative coordinates (0-1)
- Format: `x1,y1,x2,y2` (top-left to bottom-right)

### Traffic Light Timing
- Base green time: 20 seconds minimum
- Additional time: +5 seconds per 10 vehicles
- Maximum green time: 60 seconds

## 📈 Performance Metrics

The system tracks several key performance indicators:
- **Average Wait Time**: Time vehicles spend waiting at intersections
- **Vehicles Processed**: Total number of vehicles handled
- **Traffic Efficiency**: Overall system performance percentage
- **Learning Progress**: DQN agent improvement over time

## 🚨 Troubleshooting

### Common Issues

1. **"No module named 'ultralytics'"**
   ```bash
   pip install ultralytics
   ```

2. **"YOLO model not found"**
   - The system will automatically download the YOLO model on first run
   - Ensure internet connection for initial setup

3. **"Port 8000 already in use"**
   - Stop other applications using port 8000
   - Or modify the port in `app3.py` (last line)

4. **Video upload fails**
   - Check video format (MP4, AVI, MOV supported)
   - Ensure sufficient disk space
   - Verify file permissions

### Performance Tips

- Use smaller video files for faster processing
- Adjust ROI settings for better detection accuracy
- Monitor system resources during processing
- Close unnecessary applications for better performance

## 🤝 Contributing

This is an educational project demonstrating AI applications in traffic management. Feel free to:
- Report issues or bugs
- Suggest improvements
- Add new features
- Optimize performance

## 📄 License

This project is for educational and research purposes. Please ensure compliance with local regulations when using for traffic monitoring applications.

## 🙏 Acknowledgments

- **YOLO**: Object detection framework
- **FastAPI**: Modern web framework for Python
- **OpenCV**: Computer vision library
- **PyTorch**: Deep learning framework
- **Chart.js**: Data visualization library

---

**Note**: This system is designed for educational purposes and traffic analysis. For production deployment, additional safety measures and regulatory compliance may be required.