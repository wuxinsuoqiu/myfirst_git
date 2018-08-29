#_*_ coding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime


from django.db import models
from DjangoUeditor.models import UEditorField


from organization.models import CourseOrg, Teacher

# Create your models here.

class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg,verbose_name='课程机构', null=True,blank=True)
    name = models.CharField(max_length=50, verbose_name="课程名")
    desc = models.CharField(max_length=300,verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    detail = UEditorField(verbose_name="课程详情", width=600, height=300, imagePath="courses/ueditor/",
                          filePath="courses/ueditor/",default="")
    is_banner = models.BooleanField(default=False, verbose_name='是否轮播')
    teacher = models.ForeignKey(Teacher, verbose_name='讲师', null=True, blank=True)
    degree = models.CharField(choices=(("cj","初级"),("zj","中级"),("gj","高级")),max_length=2,verbose_name='难度')
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    students = models.IntegerField(default=0,verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0,verbose_name="收藏人数")
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图',max_length=100)
    click_nums = models.IntegerField(default=0,verbose_name="点击数")
    category = models.CharField(max_length=20, verbose_name="课程類別",default='後端開發')
    tag = models.CharField(max_length=10, verbose_name='課程標籤',default='')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    youneed_know = models.CharField(max_length=300, verbose_name='课程须知', default='')
    teacher_tell = models.CharField(max_length=300, verbose_name='老师告诉你', default='')

    class Meta:
         verbose_name = '课程'
         verbose_name_plural = verbose_name

    def get_zj_nums(self):
        #獲取課程章節數
        return self.lesson_set.all().count()
    #设置显示的函数名
    get_zj_nums.short_description = '章节数'


    #通过函数传递html代码
    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe('<a href="http://......">跳转</>')
    go_to.short_description = '函数跳转'


    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        #获取课程章节
        return self.lesson_set.all()


    def __unicode__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = '轮播课程'
        verbose_name_plural = verbose_name
        proxy = True #非常重要，若想配置多个model管理一张表，必须设置为True，否则django会再生成一张表


class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        #获取章节视频
        return self.video_set.all()

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name="章节",on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name="视频名")
    url = models.CharField(max_length=200,verbose_name='访问地址', default="")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name



    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    download = models.FileField(upload_to='course/resource/%Y/%m',verbose_name='资源文件',max_length=100)
    name = models.CharField(max_length=100,verbose_name="名称")
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')


    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
