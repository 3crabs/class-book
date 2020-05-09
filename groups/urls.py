from django.conf.urls import url
from django.views.generic import ListView, DetailView

from groups.models import Group

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Group.objects.all().order_by("name"), template_name="groups/index.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Group, template_name="groups/info.html")),
]
