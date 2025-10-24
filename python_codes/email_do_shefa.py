import smtplib
from email.message import EmailMessage

sender_email = "moqt_mail"
receiver_email = "drugia_mail"
password = "parolata_mi" 

smtp_server = "smtp.gmail.com"
port = 587  

msg = EmailMessage()
msg['Subject'] = "zadacha1"
msg['From'] = "moqt_mail"
msg['To'] = "drugia_mail"
msg.set_content("napravih li zadachata?")

try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")