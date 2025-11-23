import resend
import os

def send_email(to_email: str, subject: str, message: str):
    """
    Send an email using Resend API.
    Works on all cloud platforms (Render, Hugging Face, etc.)
    """
    resend.api_key = os.getenv("RESEND_API_KEY")
    
    if not resend.api_key:
        raise ValueError("RESEND_API_KEY not configured in environment variables.")
    
    # Get sender email from environment or use default
    sender_email = os.getenv("SENDER_EMAIL", "onboarding@resend.dev")

    try:
        print(f"Sending email to {to_email} via Resend API...")
        
        params = {
            "from": sender_email,
            "to": [to_email],
            "subject": subject,
            "html": f"<p>{message}</p>"
        }
        
        email = resend.Emails.send(params)
        print(f"Email sent successfully! ID: {email['id']}")
        
    except Exception as e:
        print(f"Resend API Error: {e}")
        raise e

