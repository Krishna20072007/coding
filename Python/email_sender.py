import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):
    email_message = MIMEMultipart()
    email_message["From"] = sender_email
    email_message["To"] = receiver_email
    email_message["Subject"] = subject

    email_message.attach(MIMEText(message, "plain"))
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, email_message.as_string())

sender_email = "krishnakashab@gmail.com"
sender_password = "rmxgjpaayhfcguol"
# receiver_email = input("Enter receiver's email address: ")
receiver_email = ["krishnakashab@gmail.com", "kamalmahek1610@gmail.com"]
subject = input("Enter a subject: ")
message = input("Enter a message: ")

for i in range(len(receiver_email)):
    send_email(sender_email, sender_password, str(receiver_email[i]), str(subject), str(message))
    print(f"Sent email to {receiver_email[i]}, with the subject {subject}, and body {message}")
