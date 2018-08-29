# _*_ coding: utf-8 _*_
__author__ = 'mk'
__date__ = '2018/8/9 20:31'

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequireMixin(object):

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self,request,*args,**kwargs):
        return super(LoginRequireMixin,self).dispatch(request,*args,**kwargs)