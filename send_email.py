import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Email settings
EMAIL_USER = os.getenv("EMAIL_USERNAME")
EMAIL_PASS = os.getenv("EMAIL_PASSWORD")
EMAIL_FROM = EMAIL_USER
EMAIL_TO = ["<placeholder1@example.com>", "<placeholder2@example.com>"]  # Replace with real subscriber list
EMAIL_SUBJECT = "🛍️ Fresh Deals from DailyLoots – Check Out the Latest Offers!"

# Read the latest blog content (HTML)
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Create email message
msg = MIMEMultipart("alternative")
msg["From"] = EMAIL_FROM
msg["To"] = ", ".join(EMAIL_TO)
msg["Subject"] = EMAIL_SUBJECT

part_html = MIMEText(html_content, "html")
msg.attach(part_html)

# Send the email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    print("✅ Newsletter sent successfully.")
except Exception as e:
    print(f"❌ Failed to send email: {e}")
