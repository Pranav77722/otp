---
title: OTP Backend
emoji: 🔐
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

# Flask OTP Backend (Hugging Face Spaces)

This is a Flask backend designed to send OTPs via Email (SMTP) and Firebase Email Links. It is configured for deployment on Hugging Face Spaces.

## 🚀 Deployment to Hugging Face Spaces

1.  **Create a New Space**:
    - Go to Hugging Face -> New Space.
    - Name: `otp-backend` (or similar).
    - SDK: **Docker** (Recommended) or **Gradio** (if using standard Python, but this project uses `gunicorn` so standard Python space with `Procfile` works too).
    - Select **Python** as the SDK.

2.  **Upload Files**:
    - Upload all files in this directory to the Space.

3.  **Secrets Configuration**:
    - Go to **Settings** -> **Variables and secrets**.
    - Add the following **Secrets**:
        - `SMTP_EMAIL`: Your Gmail address.
        - `SMTP_PASSWORD`: Your Gmail App Password.
    - **Important**: For Firebase, you cannot easily upload the JSON file as a secret.
        - **Option A (Recommended for HF)**: Encode the `serviceAccountKey.json` content as a Base64 string and store it as a secret named `FIREBASE_CREDENTIALS_BASE64`. Then modify `firebase_init.py` to decode it.
        - **Option B (Simpler)**: Upload `serviceAccountKey.json` directly (WARNING: NOT SECURE for public repos). If your Space is **Private**, this is acceptable.

## 🛠 Local Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Variables**:
    - Copy `.env.example` to `.env`.
    - Fill in your `SMTP_EMAIL` and `SMTP_PASSWORD`.

3.  **Firebase Setup**:
    - Place your `serviceAccountKey.json` in the root directory.

4.  **Run Locally**:
    ```bash
    python app.py
    ```

## 📡 API Usage

**Endpoint**: `POST /send-otp`

**Request**:
```json
{
  "mobile": "7028336358"
}
```

**Response**:
```json
{
  "success": true,
  "email": "khairepranav124@gmail.com",
  "mobile": "7028336358",
  "message": "OTP sent"
}
```
