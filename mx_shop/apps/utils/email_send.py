# _*_ coding: utf-8 _*_
__author__ = 'mk'
__date__ = '2018/8/7 20:01'
from random import Random
from django.core.mail import send_mail


from users.models import EmailVerifyRecord
from mx_shop.settings import EMAIL_FROM


def generate_random_str(randomlength=8):
    strs = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        strs += chars[random.randint(0,length)]
    return strs


def send_register_email(email,send_type='register'):
    email_recode = EmailVerifyRecord()
    if send_type == 'update_email':
        code = generate_random_str(4)
    else:
        code = generate_random_str(16)
    email_recode.code = code
    email_recode.email = email
    email_recode.send_type = send_type
    email_recode.save()

    email_title = ""
    email_body = ""

    if send_type == 'register':
        email_title = '慕学在线网注册激活链接'
        email_body = '请点击下面的链接激活账号:http://127.0.0.1:8000/active/{0}'.format(code)
        send_status = send_mail(email_title,email_body,EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = '慕学在线网密码重置链接'
        email_body = '请点击下面的链接重置密码:http://127.0.0.1:8000/reset/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == 'update_email':
        email_title = '慕学在线网邮箱修改验证码链接'
        email_body = '你的邮箱验证码为:{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass