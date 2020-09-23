from celery import shared_task
from django.core.mail import send_mail


@shared_task
def task_send_email():
    send_mail('Celery task worked',  # title
              'This is the body of this email',  # body
              '53027569@qq.com',  # recipient
              ['hguitar@gmail.com'])  # 收件人在一个list中
    return 'Email sent'