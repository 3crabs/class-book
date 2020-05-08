from django.db import models

from subjects.models import Subject


class Group(models.Model):
    name = models.CharField(max_length=30)
    subject = models.ManyToManyField(Subject)
