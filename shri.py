import cv2
import numpy as np
import streamlit as st
from PIL import Image
import tempfile
import base64
from io import BytesIO

# Apply custom CSS for a modern look and fixed video frame size
st.markdown(
    """
    <style>
        body {
            background-color: #e3f2fd !important;
        }
        .main-title {
            font-size: 38px;
            font-weight: bold;
            text-align: center;
            color: #0d47a1;
            padding: 12px;
            background: linear-gradient(to right, #64b5f6, #bbdefb);
            border-radius: 12px;
            margin-bottom: 20px;
        }
        .status-box {
            font-size: 22px;
            text-align: center;
            padding: 10px;
            border-radius: 8px;
            font-weight: bold;
            margin-bottom: 15px;
        }
        .anomaly {
            color: #ffffff;
            background: #d32f2f;
            box-shadow: 0px 0px 10px #b71c1c;
        }
        .normal {
            color: #ffffff;
            background: #2e7d32;
            box-shadow: 0px 0px 10px #1b5e20;
        }
        .upload-box {
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            color: #0d47a1;
            padding: 10px;
            border: 2px dashed #64b5f6;
            border-radius: 10px;
            margin-bottom: 15px;
            background: #bbdefb;
        }
        .stApp {
            background-color: #e3f2fd;
        }
        .video-frame img {
            width: 567px !important;
            height: 567px !important;
            object-fit: contain;
            border: 2px solid #0d47a1;
            border-radius: 10px;
            box-shadow: 0px 0px 8px rgba(13, 71, 161, 0.6);
            margin: 10px auto;
            display: block;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display main title
st.markdown("<h1 class='main-title'>🚨Anomaly Detection System🚨</h1>", unsafe_allow_html=True)

# File uploader with custom styling
st.markdown("<div class='upload-box'>📂Upload CCTV Footage for Anomaly Detection</div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"], label_visibility="collapsed")

# Anomaly detection logic
def detect_anomalies(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    anomaly_detected = False
    for contour in contours:
        if cv2.contourArea(contour) > 700:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)
            anomaly_detected = True
    return frame, anomaly_detected

# Main video handling logic
if uploaded_file is not None:
    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_video.write(uploaded_file.read())

    cap = cv2.VideoCapture(temp_video.name)

    status_text = st.empty()
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, anomaly = detect_anomalies(frame)

        frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)

        # Convert image to base64 for HTML embedding
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()
        encoded = base64.b64encode(img_bytes).decode()

        # Update anomaly status
        if anomaly:
            status_text.markdown("<h3 class='status-box anomaly'>🚨Anomaly Detected!🚨</h3>", unsafe_allow_html=True)
        else:
            status_text.markdown("<h3 class='status-box normal'>✅ No Anomaly Detected</h3>", unsafe_allow_html=True)

        # Display video frame at fixed size
        stframe.markdown(
            f"""
            <div class='video-frame'>
                <img src='data:image/png;base64,{encoded}' />
            </div>
            """,
            unsafe_allow_html=True
        )

    cap.release()
    temp_video.close()
