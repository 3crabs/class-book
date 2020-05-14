from django.conf.urls import url

from accounting import views

urlpatterns = [
    url(r'^rating/(?P<pk>\d+)$', view=views.save_rating, name='save'),
    url(r'^visit/(?P<pk>\d+)$', view=views.save_visit, name='save'),
]
