# _*_ coding: utf-8 _*_
__author__ = 'mk'
__date__ = '2018/8/7 11:30'

from .models import Course,Lesson,Video,CourseResource,BannerCourse
import xadmin
from organization.models import CourseOrg


#配置页面的组装,但是只可以做到单层嵌套，无法做到俩层以上嵌套
class LessonInline(object):
    model = Lesson
    extra = 0

class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    #可以将在model中写的函数也传到list中去
    list_display = ['name','desc','detail','degree','learn_times','students','fav_nums','image',
                    'click_nums','add_time','get_zj_nums','go_to']
    search_fields = ['name','desc','detail','degree','learn_times','students','fav_nums','image',
                    'click_nums']
    list_filter = ['name','desc','detail','degree','learn_times','students','fav_nums','image',
                    'click_nums','add_time']
    #设置默认排序
    ordering = ['-click_nums']
    #设置只读字段
    readonly_fields = ['click_nums',]
    #设置隐藏字段，会与只读字段冲突
    exclude = ['fav_nums']
    inlines = [LessonInline, CourseResourceInline] #用于配置页面的组装
    #设置在列表页可以直接修改的字段
    list_editable = ['degree','desc']
    #设置定时刷新
    refresh_times = [3, 5]
    style_fields = {'detail':'ueditor'}
    import_excel = True

    # 重载queryset方法以设置model的显示内容
    def queryset(self):
        qs = super(CourseAdmin,self).queryset()
        return qs.filter(is_banner=False)

    #重载save_models方法用于在model保存时定义自己的逻辑
    def save_models(self):
        #在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        #  导入逻辑
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)




#设置多个model控制一张表，每个model展示数据不一样
class BannerCourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','students','fav_nums','image',
                    'click_nums','add_time']
    search_fields = ['name','desc','detail','degree','learn_times','students','fav_nums','image',
                    'click_nums']
    list_filter = ['name','desc','detail','degree','learn_times','students','fav_nums','image',
                    'click_nums','add_time']
    #设置默认排序
    ordering = ['-click_nums']
    #设置只读字段
    readonly_fields = ['click_nums',]
    #设置隐藏字段，会与只读字段冲突
    exclude = ['fav_nums']
    inlines = [LessonInline, CourseResourceInline] #用于配置页面的组装

    # 重载queryset方法以设置model的显示内容
    def queryset(self):
        qs = super(BannerCourseAdmin,self).queryset()
        return qs.filter(is_banner=True)




class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']



class ViedoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'download', 'name','add_time']
    search_fields = ['course', 'download', 'name']
    list_filter = ['course', 'download', 'name','add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(BannerCourse,BannerCourseAdmin)
xadmin.site.register(Video,ViedoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
