from django.shortcuts import render

from accounting.models import Attendance, Result
from groups.models import Group
from subjects.models import Subject, Task, Lesson


def subjects(request):
    if request.POST:
        item = Subject(
            name=request.POST['name'],
            level_3=request.POST['level_3'],
            level_4=request.POST['level_4'],
            level_5=request.POST['level_5'],
        )
        item.save()
    object_list = Subject.objects.all().order_by("name")
    return render(request, 'subjects/index.html', locals())


def subject(request, pk):
    subject = Subject.objects.get(id=pk)

    if 'delete' in request.POST:
        subject.delete()
        object_list = Subject.objects.all().order_by("name")
        return render(request, 'subjects/index.html', locals())

    subject = Subject.objects.get(id=pk)
    return render(request, 'subjects/info.html', locals())


def subject_tasks(request, pk):
    if request.POST:
        item = Task(
            name=request.POST['name'],
            deadline=request.POST['date'],
            subject_id=pk,
        )
        item.save()
        groups = Group.objects.all()
        for group in groups:
            if item.subject in group.subjects.all():
                for student in group.student_set.all():
                    result = Result()
                    result.student = student
                    result.task = item
                    result.save()
    subject = Subject.objects.get(id=pk)
    return render(request, 'subjects/info.html', locals())


def subject_lessons(request, pk):
    if request.POST:
        item = Lesson(
            name=request.POST['name'],
            date=request.POST['date'],
            subject_id=pk,
        )
        item.save()
        groups = Group.objects.all()
        for group in groups:
            if item.subject in group.subjects.all():
                for student in group.student_set.all():
                    attendance = Attendance()
                    attendance.student = student
                    attendance.lesson = item
                    attendance.save()
    subject = Subject.objects.get(id=pk)
    return render(request, 'subjects/info.html', locals())


def subject_task(request, pk, id):
    task = Task.objects.get(id=id)

    if 'delete' in request.POST:
        task.delete()

    subject = Subject.objects.get(id=pk)
    return render(request, 'subjects/info.html', locals())


def subject_lesson(request, pk, id):
    lesson = Lesson.objects.get(id=id)

    if 'delete' in request.POST:
        lesson.delete()

    subject = Subject.objects.get(id=pk)
    return render(request, 'subjects/info.html', locals())
