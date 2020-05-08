from django.conf.urls import url
from django.views.generic import ListView

from groups.models import Group

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Group.objects.all().order_by("name"), template_name="groups/index.html")),
]
