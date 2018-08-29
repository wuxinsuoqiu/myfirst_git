#_*_ coding:utf-8 _*_
"""mx_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
import xadmin
from users.views import LoginView,RegisterView,ActivateUserView,ForgetView,\
    ResetView,ModifyPwdView, LogoutView,IndexView
from mx_shop.settings import MEDIA_ROOT, STATIC_ROOT


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),

    #不安全的登录
    # url(r'^login/$', LoginUnsafeView.as_view(), name='login'),

    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$',ActivateUserView.as_view(),name='active'),
    url(r'^forget/$', ForgetView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<active_code>.*)/$',ResetView.as_view(),name='reset'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),
    # url(r'^orgs/list/$', OrgView.as_view(),name='course_list'),
    #课程机构url配置
    url(r'^org/', include('organization.urls', namespace='org')),
    #课程相关url配置
    url(r'^course/', include('courses.urls', namespace='course')),
    #用户相关url配置
    url(r'^users/', include('users.urls', namespace='users')),

    #富文本相关url
    url(r'^ueditor/',include('DjangoUeditor.urls' )),

    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*$)',serve, {"document_root":MEDIA_ROOT}),

    # 配置静态文件的访问处理函数
    url(r'^static/(?P<path>.*$)', serve, {"document_root": STATIC_ROOT}),

]

#全局404页面配置
handler404 = 'users.views.page_not_found'

#全局500页面配置
handler500 = 'users.views.page_error'

#全局403页面配置
handler403 =  'users.views.server_error'