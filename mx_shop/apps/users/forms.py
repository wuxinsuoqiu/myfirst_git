# _*_ coding: utf-8 _*_
__author__ = 'mk'
__date__ = '2018/8/7 17:36'

from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'invalid':'邮箱错误'})
    password = forms.CharField(required=True, min_length=5, error_messages={'invalid':'密码错误'})
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'invalid': '邮箱错误'})
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5, error_messages={'invalid': '密码错误'})
    password2 = forms.CharField(required=True, min_length=5, error_messages={'invalid':'密码错误'})


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name','gender','birthday','address','moblie']

