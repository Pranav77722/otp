from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Import modules
from db import get_email_from_mobile
from otp_service import generate_otp, generate_firebase_link
from email_service import send_email
import firebase_init # Initializes Firebase

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

@app.route('/send-otp', methods=['POST'])
def send_otp():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "message": "Invalid JSON body"}), 400

        mobile = data.get('mobile')
        if not mobile:
            return jsonify({"success": False, "message": "Mobile number is required"}), 400

        # 1. Lookup email
        email = get_email_from_mobile(mobile)
        if not email:
            return jsonify({"success": False, "message": "Mobile number not registered"}), 404

        # 2. Generate OTP
        otp = generate_otp()
        
        # Optional: Generate Firebase Link (if serviceAccountKey.json is present)
        # firebase_link = generate_firebase_link(email) 
        # For now, we just use the numeric OTP as requested for the main flow.

        # 3. Prepare Email
        subject = "Your Login OTP"
        body = f"Your OTP is: {otp}\n\nThis code is valid for 10 minutes."

        # 4. Send Email
        try:
            send_email(email, subject, body)
        except Exception as e:
            return jsonify({"success": False, "message": f"Failed to send email: {str(e)}"}), 500

        # 5. Return Success Response
        return jsonify({
            "success": True,
            "email": email,
            "mobile": mobile,
            "message": "OTP sent"
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Internal Server Error: {str(e)}"}), 500

if __name__ == '__main__':
    # Run locally
    app.run(host='0.0.0.0', port=5000, debug=False)
