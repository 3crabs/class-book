from django.shortcuts import render

from groups.models import Group, Student
from subjects.models import Subject


def groups(request):
    if request.POST:
        item = Group(name=request.POST['name'])
        item.save()
    object_list = Group.objects.all().order_by("name")
    return render(request, 'groups/index.html', locals())


def group(request, pk):
    group = Group.objects.get(id=pk)

    if 'delete' in request.POST:
        group.delete()
        object_list = Group.objects.all().order_by("name")
        return render(request, 'groups/index.html', locals())

    group = Group.objects.get(id=pk)
    subject_list = Subject.objects.all().order_by("name")
    return render(request, 'groups/info.html', locals())


def group_students(request, pk):
    if request.POST:
        item = Student(
            name=request.POST['name'],
            email=request.POST['email'],
            group_id=pk,
        )
        item.save()
    group = Group.objects.get(id=pk)
    return render(request, 'groups/info.html', locals())


def group_student(request, pk, id):
    student = Student.objects.get(id=id)

    if 'delete' in request.POST:
        student.delete()

    group = Group.objects.get(id=pk)
    subject_list = Subject.objects.all().order_by("name")
    return render(request, 'groups/info.html', locals())


def group_subjects(request, pk):
    if request.POST:
        group = Group.objects.get(id=pk)
        subject = Subject.objects.get(id=request.POST['subject'])
        group.subjects.add(subject)
        group.save()
    group = Group.objects.get(id=pk)
    subject_list = Subject.objects.all().order_by("name")
    return render(request, 'groups/info.html', locals())


def group_subject(request, pk, id):
    if 'delete' in request.POST:
        group = Group.objects.get(id=pk)
        subject = Subject.objects.get(id=id)
        group.subjects.remove(subject)
        group.save()
        group = Group.objects.get(id=pk)
        subject_list = Subject.objects.all().order_by("name")
        return render(request, 'groups/info.html', locals())
    else:
        group = Group.objects.get(id=pk)
        return render(request, 'accouting/index.html', locals())




