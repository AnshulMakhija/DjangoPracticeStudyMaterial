from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task(subject, message, to_email):
    send_mail(
        subject,
        message,
        'anshul.glsbca20@gmail.com', 
        [to_email],
        fail_silently=False
    )
    return f"Email sent to {to_email}"
