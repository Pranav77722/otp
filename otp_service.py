import secrets
import string
from firebase_admin import auth

def generate_otp(length: int = 6) -> str:
    """
    Generate a secure numeric OTP of given length.
    """
    return ''.join(secrets.choice(string.digits) for _ in range(length))

def generate_firebase_link(email: str) -> str:
    """
    Generate a Firebase Email Sign-In Link.
    Returns the link or None if failed.
    """
    try:
        action_code_settings = auth.ActionCodeSettings(
            url='http://localhost:5000/finishSignUp', # Replace with your actual frontend URL
            handle_code_in_app=True,
            ios_bundle_id='com.example.ios',
            android_package_name='com.example.android',
            android_install_app=True,
            android_minimum_version='12'
        )
        
        link = auth.generate_sign_in_with_email_link(email, action_code_settings)
        return link
    except Exception as e:
        print(f"Error generating Firebase link: {e}")
        return None
