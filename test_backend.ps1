$body = @{
    mobile = "7028336358"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/send-otp" -Method Post -Body $body -ContentType "application/json"
