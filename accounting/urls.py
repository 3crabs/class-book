from django.conf.urls import url

from accounting import views

urlpatterns = [
    url(r'^$', view=views.save),
]
