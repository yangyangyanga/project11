from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^students/$', views.students),
    url(r'^addstudent/$', views.addstudent),
    url(r'^addstudent1/$', views.addstudent1),

    url(r'^students1/$', views.students1),
    url(r'^students2/$', views.students2),
    url(r'^stupage/(\d+)$', views.stupage),
    url(r'^studentsearch/$', views.studentsearch),
    url(r'^grades/$', views.grades),
]