from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import base64

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Gemini API credentials (replace with actual credentials)
GEMINI_API_URL = "https://api.gemini.com/scratch-detection"
GEMINI_API_KEY = "your_gemini_api_key_here"

@app.route('/detect-scratches', methods=['POST'])
def detect_scratches():
    try:
        # Receive the image data as a base64 string from the webpage
        image_data = request.json.get("imageData")

        if not image_data:
            return jsonify({"error": "No image data provided"}), 400

        # Decode the base64 image
        image_bytes = base64.b64decode(image_data.split(",")[1])

        # Prepare the request payload for Gemini API
        headers = {
            "Authorization": f"Bearer {GEMINI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "image": base64.b64encode(image_bytes).decode("utf-8"),
            "parameters": {"detect_scratches": True, "measure_lengths": True}
        }

        # Send the image to Gemini API
        response = requests.post(GEMINI_API_URL, json=payload, headers=headers)

        # Parse the response
        if response.status_code == 200:
            result = response.json()
            return jsonify(result)
        else:
            return jsonify({"error": "Gemini API error", "details": response.json()}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
