"""
Mock database for OTP API.
Stores mobile to email mappings.
"""

# Dummy database: Mobile -> Email
USERS = {
    "9309192611": "test@gmail.com",
    "7028336358": "khairepranav124@gmail.com"
}

def get_email_from_mobile(mobile: str) -> str:
    """
    Look up email by mobile number.
    Returns None if mobile not found.
    """
    return USERS.get(mobile)
