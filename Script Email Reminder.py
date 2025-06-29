import csv
import smtplib
from email.message import EmailMessage
from datetime import datetime

# Configuration de l'email
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"  # Utilise un mot de passe d'application si tu as l'authentification à deux facteurs

def send_email(to, subject, body):
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print(f"Email sent to {to}")

# Lire le fichier CSV manuellement
today = datetime.now().date().isoformat()

with open(r"C:\Users\user\Desktop\CODEAlpha\reminders.csv.csv", newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['date'] == today:
            send_email(row['email'], row['subject'], row['body'])
