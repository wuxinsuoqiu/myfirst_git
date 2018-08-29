# _*_ coding: utf-8 _*_
__author__ = 'mk'
__date__ = '2018/8/7 11:46'

import xadmin
from .models import CityDict,CourseOrg,Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

    model_icon = 'fa fa-user-plus'

class CourseOrgAdmin(object):
    list_display = ['name', 'desc','click_nums','fav_nums','image','address','city', 'add_time']
    search_fields = ['name', 'desc','click_nums','fav_nums','image','address','city']
    list_filter = ['name', 'desc','click_nums','fav_nums','image','address','city', 'add_time']
    #设置搜索方式，设置在外键处，用于设置搜索主键的加载方式
    relfield_style = 'fk-ajax' #设置为ajax的搜索方式


class TeaherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points',
                    'click_nums','fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points',
                    'click_nums','fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points',
                    'click_nums','fav_nums', 'add_time']


xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeaherAdmin)