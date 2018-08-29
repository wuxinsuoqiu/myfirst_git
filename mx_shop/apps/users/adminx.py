# _*_ coding: utf-8 _*_
__author__ = 'mk'
__date__ = '2018/8/7 10:40'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord,Banner,UserProfile
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row


class UserProfileAdmin(UserAdmin):
    """
    重载页面布局方法
    """
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('first_name', 'last_name'),
                             'email'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '慕学后台管理系统'
    site_footer = "慕学在线网"
    menu_style = "accordion"
    model_icon = 'fa fa-behance-square'


class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','sent_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','sent_time']
    model_icon = 'fa fa-assistive-listening-systems'


class BannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']
    #model_icon = 'fa fa-user' 使用 Font Awesome编辑图标

# class

"""
当前版本已经卸载了，所以不必再卸载
原理为再xadmin.plugins.auth下将原来admin的User改为当前的UserProfile
from django.contrib.auth.models import User
xadmin.site.unregister(User)
xadmin.site.register(UserProfile,UserProfileAdmin) 当前版本已经关联了，可以不必再关联了
"""
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
