from flask_mail import Message, Mail
from twilio.rest import Client
from config import Config

mail = Mail()

def send_email(recipient, subject, body):
    # Send email notifications
    msg = Message(subject, sender=Config.MAIL_DEFAULT_SENDER, recipients=[recipient])
    msg.body = body
    mail.send(msg)

def send_sms(recipient, body):
    # Send SMS notifications
    client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        from_=Config.TWILIO_PHONE_NUMBER,
        to=recipient
    )
    return message.sid
