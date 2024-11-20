import os
from django.core.mail import EmailMessage
import random
from django.conf import settings
from .models import User,OneTimePassword

def generateOtp():
    otp=""
    for i in range(6):
        otp+=str(random.randint(1,9))
    return otp
def send_code_to_user(email):
    subject="One time passcode for Email verification"
    otp_code=generateOtp()
    print(otp_code)
    user=User.objects.get(email=email)
    current_site="cutethamizha.com"
    email_body=f"Hi{user.first_name}thanks for signing up {current_site} please verify your email with the \n one time passcode{otp_code}"
    from_email=os.getenv("USER_EMAIL")
    OneTimePassword.objects.create(user=user,code=otp_code)
    send_mail=EmailMessage(subject=subject,body=email_body,from_email=from_email,to={email})
    send_mail.send(fail_silently=True) 
    
def send_normal_email(data):
    email=EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        from_email=settings.EMAIL_HOST_USER,
        to=[data['to_email']]
    )
    email.send()