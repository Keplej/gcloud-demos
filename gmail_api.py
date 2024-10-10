import os
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from google_apis import create_service

def init_gmail_service(client_file, api_name='gmail', api_version='v1', scopes=['https://mail.google.com/']):
    """Initializing the google api service specifically with gmail"""
    return create_service(client_file, api_name, api_version, scopes)


def get_gmail_user_profile(service):
    """Get the Gmail user profile to verify the connection"""
    try:
        profile = service.users().getProfile(userId='me').execute()
        print("Gmail User Profile:")
        print(f"Email: {profile['emailAddress']}")
        print(f"Messages Total: {profile['messagesTotal']}")
        print(f"Threads Total: {profile['threadsTotal']}")
    except Exception as e:
        print(f"An error occurred: {e}")

# TODO: Work on this and improve it
def send_email(service):
    """Get the Gmail api user to send emails"""
    subject = ''
    message = MIMEMultipart()
    message['to'] = '' # Email Address goes here
    message['from'] = '' # Email Address goes here
    message['subject'] = subject

    message_text = f""
    message.attach(MIMEText(message_text, 'plain'))

    # Convert message to raw format
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    try:
        message = service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        print('email was successfully sent')
    except Exception as e:
        print("An error occurred in email_system:", e)
