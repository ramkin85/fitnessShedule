from flask.ext.mail import Message
from app import mail
from config import ADMINS
from flask import render_template
from threading import Thread
from app.decorators import async


@async
def send_async_mail(msg):
    mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_mail(msg)


def admin_notification(subject, adminMail, client_name, client_phone, client_message):
    send_email(subject or "[Fitness shedule] New request from client!",
               ADMINS[0],
               [adminMail or ADMINS[1]],
               render_template("notification_email.txt",
                               client_name=client_name, client_phone=client_phone, client_message=client_message),
               render_template("notification_email.html",
                               client_name=client_name, client_phone=client_phone, client_message=client_message))


def user_register_notification(user):
    send_email("[Fitness shedule] You are registered!",
               ADMINS[0],
               [user.email],
               render_template("follower_email.txt",
                               user=user, follower=user),
               render_template("follower_email.html",
                               user=user, follower=user))
