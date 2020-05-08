from django.conf.urls import url
from django.views.generic import ListView

from .models import Subject

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Subject.objects.all().order_by("name"), template_name="subjects/index.html")),
]
