import os
from dotenv import load_dotenv

load_dotenv() # This loads the variables from .env

# Now you can use them safely
api_key = os.getenv("OPENAI_API_KEY")


import cv2
import google.generativeai as genai

class VisionModule:
    def __init__(self):
        # Configure Gemini 3 Flash
        genai.configure(api_key="YOUR_GEMINI_API_KEY")
        self.model = genai.GenerativeModel('gemini-3-flash')
        self.cap = cv2.VideoCapture(0)

    def get_pose_analysis(self):
        ret, frame = self.cap.read()
        if not ret: return None

        # In a real VLA system, we send frames to Gemini for pose matching
        # or use MediaPipe locally and send summaries to Gemini
        _, buffer = cv2.imencode('.jpg', frame)

        # Pseudo-logic for Gemini 3 Flash analysis
        prompt = "Analyze this dance frame. Is the spine straight? Return coordinates."
        # response = self.model.generate_content([prompt, buffer])

        # Simulating returned Pose Score
        return {"pose_accuracy": 0.85, "timestamp": cv2.getTickCount()}

    def release(self):
        self.cap.release()
