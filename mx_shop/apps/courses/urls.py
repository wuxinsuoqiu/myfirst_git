# _*_ coding: utf-8 _*_
__author__ = 'mk'
__date__ = '2018/8/9 12:52'

from django.conf.urls import url, include


from courses.views import CourseListView,CourseDetailView,CourseInfoView,CommentsView,AddCommentView,CourseVideoView


urlpatterns = [
    #课程列表页
    url(r'^list/$',CourseListView.as_view(),name='course_list'),
    #课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
    #
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),
    #课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name='course_comment'),
    # 添加课程评论
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),

    url(r'^video/(?P<video_id>\d+)/$', CourseVideoView.as_view(), name='course_video'),
]