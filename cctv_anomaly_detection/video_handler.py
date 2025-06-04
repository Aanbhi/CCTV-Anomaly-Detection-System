import cv2
import tempfile

def save_uploaded_file(uploaded_file):
    temp_video = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_video.write(uploaded_file.read())
    temp_video.close()
    return temp_video.name

def open_video_capture(video_path):
    return cv2.VideoCapture(video_path)
