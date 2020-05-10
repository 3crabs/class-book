from django.conf.urls import url
from django.views.generic import ListView

from groups.models import Student

urlpatterns = [
    url(r'^(?P<pk>\d+)$',
        ListView.as_view(queryset=Student.objects.all().order_by("name"), template_name="accouting/attendances.html")),
]
