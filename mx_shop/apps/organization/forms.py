# _*_ coding: utf-8 _*_
__author__ = 'mk'
__date__ = '2018/8/8 19:24'
import re
from django import forms


from operations.models import UserAsk

# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True,min_length=2, max_length=20)
#     phone = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True,max_length=5, min_length=50)


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        #验证手机号码是否合法
       mobile = self.cleaned_data['mobile']
       REGEX_MOBILE = '^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'
       p = re.compile(REGEX_MOBILE)
       if p.match(mobile):
           return mobile
       else:
           raise forms.ValidationError('手机号码非法',code='mobile_invalid')