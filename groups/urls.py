from django.conf.urls import url

from groups import views

urlpatterns = [
    url(r'^$', views.groups, name='groups'),
    url(r'^(?P<pk>\d+)$', views.group, name='group'),
    url(r'^(?P<pk>\d+)/students$', views.group_students, name='group_students'),
    url(r'^(?P<pk>\d+)/subjects$', views.group_subjects, name='group_subjects'),
    url(r'^(?P<pk>\d+)/students/(?P<id>\d+)$', views.group_student, name='group_student'),
    url(r'^(?P<pk>\d+)/subjects/(?P<id>\d+)$', views.group_subject, name='group_subject'),
]
