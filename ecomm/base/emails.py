from django.conf import settings
from django.core.mail import send_mail
def send_account_activation_email(email,email_token):
   # msg = Message('Account Activation',sender='<EMAIL>',recipients=[email])
   subject='Activate your Account'
   email_from=settings.EMAIL_HOST_USER
   message=f'Hey buddy click on this link to Activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
   send_mail(subject , message , email_from , [email])