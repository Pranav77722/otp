import firebase_admin
from firebase_admin import credentials
import os

def initialize_firebase():
    """
    Initialize Firebase Admin SDK.
    Checks for serviceAccountKey.json.
    """
    try:
        # Check if already initialized to avoid errors on re-import
        if not firebase_admin._apps:
            # Path to your service account key file
            # In Hugging Face, ensure this file is uploaded or handled via secrets
            cred_path = "serviceAccountKey.json"
            
            if os.path.exists(cred_path):
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)
                print("Firebase initialized successfully.")
            else:
                print("Warning: serviceAccountKey.json not found. Firebase features will not work.")
    except Exception as e:
        print(f"Failed to initialize Firebase: {e}")

# Initialize on module import
initialize_firebase()
