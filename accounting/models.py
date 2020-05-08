from datetime import date

from django.db import models

from groups.models import Student
from subjects.models import Lesson, Task


class Attendance(models.Model):
    visit = models.BooleanField(default=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Result(models.Model):
    rating = models.FloatField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
