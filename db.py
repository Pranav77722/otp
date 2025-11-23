"""
Mock database for OTP API.
Stores mobile to email mappings.
"""

# Dummy database: Mobile -> Email
USERS = {
    "9657329173": "ap8548328@gmail.com",
    "9699883753": "adi.akolkar12@gmail.com"
}

def get_email_from_mobile(mobile: str) -> str:
    """
    Look up email by mobile number.
    Returns None if mobile not found.
    """
    return USERS.get(mobile)
