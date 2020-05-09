from django.db import models

from subjects.models import Subject


class Group(models.Model):
    name = models.CharField(max_length=30)
    subjects = models.ManyToManyField(Subject)


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
