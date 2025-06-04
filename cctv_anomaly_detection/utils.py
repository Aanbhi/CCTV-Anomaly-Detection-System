import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import base64

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

def convert_image_to_base64(frame_rgb):
    img = Image.fromarray(frame_rgb)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode()
    return encoded
