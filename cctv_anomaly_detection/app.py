import streamlit as st
import cv2
from PIL import Image
from css import load_custom_css
from utils import detect_anomalies, convert_image_to_base64
from video_handler import save_uploaded_file, open_video_capture

# Load CSS
st.markdown(load_custom_css(), unsafe_allow_html=True)

# Title and Upload UI
st.markdown("<h1 class='main-title'>🚨Anomaly Detection System🚨</h1>", unsafe_allow_html=True)
st.markdown("<div class='upload-box'>📂Upload CCTV Footage for Anomaly Detection</div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload Video", type=["mp4", "avi", "mov"], label_visibility="collapsed")

# Main Logic
if uploaded_file is not None:
    video_path = save_uploaded_file(uploaded_file)
    cap = open_video_capture(video_path)

    status_text = st.empty()
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, anomaly = detect_anomalies(frame)
        frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
        encoded = convert_image_to_base64(frame_rgb)

        # Show Status
        if anomaly:
            status_text.markdown("<h3 class='status-box anomaly'>🚨Anomaly Detected!🚨</h3>", unsafe_allow_html=True)
        else:
            status_text.markdown("<h3 class='status-box normal'>✅ No Anomaly Detected</h3>", unsafe_allow_html=True)

        # Show Frame
        stframe.markdown(
            f"<div class='video-frame'><img src='data:image/png;base64,{encoded}' /></div>",
            unsafe_allow_html=True
        )

    cap.release()
