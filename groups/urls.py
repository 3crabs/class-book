from django.conf.urls import url

from groups import views

urlpatterns = [
    url(r'^$', views.groups, name='groups'),
    url(r'^(?P<pk>\d+)$', views.group, name='group'),
]
