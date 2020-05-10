from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.subjects, name='subjects'),
    url(r'^(?P<pk>\d+)$', views.subject, name='subject'),
]
