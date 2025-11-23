---
title: OTP Backend
emoji: 🔐
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

# Flask OTP Backend

A Flask-based REST API that sends OTPs (One-Time Passwords) via email. The API accepts a mobile number, looks up the associated email from a database, generates a 6-digit OTP, and sends it via Resend API.

## 🚀 Features

- Mobile number to email lookup
- 6-digit OTP generation
- Email delivery via Resend API
- CORS enabled for frontend integration
- Production-ready with Gunicorn
- Deployable to Render.com

## 📋 Prerequisites

- Python 3.10+
- Resend API account (free tier available)
- Git and GitHub account
- Render.com account (for deployment)

## 🛠 Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Pranav77722/otp.git
cd otp
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Get Resend API Key

1. Sign up at [resend.com](https://resend.com)
2. Go to [API Keys](https://resend.com/api-keys)
3. Click **"Create API Key"**
4. Name: `OTP Backend`
5. Permission: **Full Access**
6. Copy the API key (starts with `re_...`)

### 4. Configure Environment Variables

Create a `.env` file:

```bash
cp .env.example .env
```

Edit `.env` and add your Resend API key:

```
RESEND_API_KEY=re_your_actual_api_key_here
SENDER_EMAIL=onboarding@resend.dev
```

### 5. Run Locally

```bash
python app.py
```

Server will start at `http://localhost:5000`

## 🧪 Testing

Test the API using PowerShell:

```powershell
$body = @{
    mobile = "9657329173"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/send-otp" -Method Post -Body $body -ContentType "application/json"
```

Or using cURL:

```bash
curl -X POST http://localhost:5000/send-otp \
  -H "Content-Type: application/json" \
  -d '{"mobile":"9657329173"}'
```

Expected response:

```json
{
  "success": true,
  "email": "ap8548328@gmail.com",
  "mobile": "9657329173",
  "message": "OTP sent"
}
```

## 🌐 Deploy to Render

### Step 1: Push Code to GitHub

```bash
git add .
git commit -m "Deploy OTP backend"
git push origin main
```

### Step 2: Create Render Web Service

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `otp-backend`
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

### Step 3: Add Environment Variables

In Render Settings → Environment:

1. Click **"Add Environment Variable"**
2. Add:
   - **Key**: `RESEND_API_KEY`
   - **Value**: Your Resend API key (from step 3 above)
3. Click **"Save Changes"**

Render will automatically deploy your app!

### Step 4: Test Production API

Your API will be available at: `https://your-service-name.onrender.com`

Test it:

```powershell
$body = @{
    mobile = "9657329173"
} | ConvertTo-Json

Invoke-RestMethod -Uri "https://your-service-name.onrender.com/send-otp" -Method Post -Body $body -ContentType "application/json"
```

## 📡 API Reference

### Endpoint: POST /send-otp

**Request:**

```json
{
  "mobile": "9657329173"
}
```

**Success Response (200):**

```json
{
  "success": true,
  "email": "ap8548328@gmail.com",
  "mobile": "9657329173",
  "message": "OTP sent"
}
```

**Error Responses:**

**400 - Invalid Request**
```json
{
  "success": false,
  "message": "Mobile number is required"
}
```

**404 - Mobile Not Found**
```json
{
  "success": false,
  "message": "Mobile number not registered"
}
```

**500 - Server Error**
```json
{
  "success": false,
  "message": "Failed to send email: ..."
}
```

## 📚 Database

Current users in `db.py`:

| Mobile Number | Email                    |
|---------------|--------------------------|
| 9657329173    | ap8548328@gmail.com      |
| 9699883753    | adi.akolkar12@gmail.com  |

To add more users, edit `db.py`:

```python
USERS = {
    "9657329173": "ap8548328@gmail.com",
    "9699883753": "adi.akolkar12@gmail.com",
    "1234567890": "newuser@example.com"  # Add new entry
}
```

## 🔧 Configuration

### Sender Email (Optional)

By default, emails are sent from `onboarding@resend.dev`.

To use a custom sender:
1. Own a domain (e.g., `yourdomain.com`)
2. Verify it in Resend dashboard
3. Add environment variable:
   ```
   SENDER_EMAIL=noreply@yourdomain.com
   ```

## ⚠️ Important Notes

- **Do NOT commit `.env`** to GitHub (it's in `.gitignore`)
- **Free Resend tier**: 3,000 emails/month, 100/day
- **Render free tier**: May spin down after inactivity (30 sec startup)
- For production, consider upgrading to paid tiers

## 📁 Project Structure

```
otp/
├── app.py              # Main Flask application
├── db.py               # User database (mobile → email)
├── email_service.py    # Resend email integration
├── otp_service.py      # OTP generation logic
├── firebase_init.py    # Firebase Admin SDK setup (optional)
├── requirements.txt    # Python dependencies
├── Procfile           # Render/Heroku configuration
├── Dockerfile         # Docker configuration
├── runtime.txt        # Python version
├── .env.example       # Environment template
└── README.md          # This file
```

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

## 📄 License

MIT License

## 🆘 Support

For issues or questions:
- GitHub Issues: [Create an issue](https://github.com/Pranav77722/otp/issues)
- Email: Contact repository owner

---

**Made with ❤️ using Flask and Resend**
