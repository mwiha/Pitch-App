from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**Alice):
    sender_email ="alicemwihaki99@gmail.com"

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**Alice)
    email.html = render_template(template + ".html",**Alice)
    mail.send(email)