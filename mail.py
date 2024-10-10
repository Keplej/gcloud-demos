from gmail_api import init_gmail_service, get_gmail_user_profile, send_email

client_file = 'client_secret.json'
service = init_gmail_service(client_file)
# user_email = get_gmail_user_profile(service)
sending = send_email(service)