from djangoair.celery import app
from django.core.mail import EmailMessage

@app.task()
def send_mail_task(email, content):
    msg = EmailMessage()
    msg.subject = 'Airplane ticket'
    msg.from_email = 'info@rns.pp.ua'
    msg.to.append(email)
    msg.body = content
    msg.content_subtype = 'html'
    msg.send()