🚨 Anomaly Detection System 

This project is a real-time anomaly detection system designed to analyze CCTV footage and highlight unusual activity. It uses OpenCV for frame processing and Streamlit for a modern, interactive web interface.


🔍 Features

1. Upload and analyze CCTV videos

2. Detect anomalies based on motion and contour detection

3. Real-time frame display with highlighted anomalies

4. Clean, responsive UI with custom CSS styling


📸 Demo UI

Sample UI interface with detected anomaly bounding boxes.


🛠️ Requirements

Install the necessary packages using pip:-

pip install streamlit opencv-python-headless numpy Pillow


🚀 How to Run

1. Clone the repository:

git clone https://github.com/Aanbhi/CCTV-Anomaly-Detection-System.git
cd CCTV-Anomaly-Detection-System

2. Run the Streamlit app:

streamlit run app.py

3. Upload a video file (.mp4, .avi, .mov) through the interface to begin anomaly detection.


📦 File Structure

├── app.py             # Main Streamlit application

├── README.md          # Project documentation

└── requirements.txt   # Python dependencies (optional)


📚 How It Works

1. Frames from uploaded videos are converted to grayscale.

2. A threshold is applied to highlight bright regions.

3. Contours are extracted, and any region with significant area (>700 pixels) is flagged as an anomaly.

4. Anomalies are highlighted with red bounding boxes on the video frame.


💡 Future Improvements

1. Use deep learning models like YOLOv8 for better anomaly classification.

2. Add multiple anomaly classes (fire, fight, accident, theft).

3. Store results in a database and provide reporting/dashboard capabilities.


👨‍💻 Author 
Developed by ANBHI THAKUR
