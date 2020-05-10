from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.subjects, name='subjects'),
    url(r'^(?P<pk>\d+)$', views.subject, name='subject'),
    url(r'^(?P<pk>\d+)/tasks$', views.subject_tasks, name='subject_tasks'),
    url(r'^(?P<pk>\d+)/tasks/(?P<id>\d+)$', views.subject_task, name='subject_task'),
    url(r'^(?P<pk>\d+)/lessons$', views.subject_lessons, name='subject_lessons'),
    url(r'^(?P<pk>\d+)/lessons/(?P<id>\d+)$', views.subject_lesson, name='subject_lesson'),
]
