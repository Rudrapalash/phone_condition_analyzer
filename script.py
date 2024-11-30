from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import base64

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Configure the API with the API key
genai.configure(api_key="AIzaSyCxuat-pKZfi7hAaKQ5HMP_zs7M4H7TpbE")

# Create the generative model instance for the gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/detect-scratches', methods=['POST'])
def detect_scratches():
    try:
        # Receive the image data as a base64 string from the request
        image_data = request.json.get("imageData")

        if not image_data:
            return jsonify({"error": "No image data provided"}), 400

        # Decode the base64 image data
        image_bytes = base64.b64decode(image_data.split(",")[1])

        # Here you would convert the image to a format that the model can process,
        # but since this model is for generating text, consider adding another step
        # to send the image for processing if needed. For this example, we'll simulate
        # a response based on a generic scratch detection request.
        
        # Generate content with the model as an example
        response = model.generate_content("Detect scratches in the provided image")

        # Return the simulated response from the model
        return jsonify({"message": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
