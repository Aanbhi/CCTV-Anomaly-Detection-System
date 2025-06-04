def load_custom_css():
    return """
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
    """
