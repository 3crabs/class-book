from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from accounting.models import Attendance, Result
from class_book import settings
from groups.models import Group, Student
from subjects.models import Subject

import xlwt


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
        subjects = group.subjects.all()
        for subject in subjects:
            for lesson in subject.lesson_set.all():
                attendance = Attendance()
                attendance.student = item
                attendance.lesson = lesson
                attendance.save()
            for task in subject.task_set.all():
                result = Result()
                result.student = item
                result.task = task
                result.save()
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
        for student in group.student_set.all():
            for lesson in subject.lesson_set.all():
                attendance = Attendance()
                attendance.student = student
                attendance.lesson = lesson
                attendance.save()
            for task in subject.task_set.all():
                result = Result()
                result.student = student
                result.task = task
                result.save()
    group = Group.objects.get(id=pk)
    subject_list = Subject.objects.all().order_by("name")
    return render(request, 'groups/info.html', locals())


def group_subject(request, pk, id):
    subject = Subject.objects.get(id=id)
    if 'delete' in request.POST:
        group = Group.objects.get(id=pk)
        group.subjects.remove(subject)
        group.save()
        group = Group.objects.get(id=pk)
        subject_list = Subject.objects.all().order_by("name")
        return render(request, 'groups/info.html', locals())
    else:
        group = Group.objects.get(id=pk)
        itogs = {}
        for student in group.student_set.all():
            itogs[student.id] = student.id + 1
        print(itogs)
        return render(request, 'accouting/index.html', locals())


def create_xls_(group, subject):
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet(group.name)
    sheet.write(0, 0, "Успеваемость группы " + group.name + " по предмету " + subject.name)
    row = 1
    col = 0
    sheet.write(row, col, "Посещаемость")
    row += 1
    sheet.write(row, col, "Студент")
    col += 1
    for lesson in subject.lesson_set.all():
        sheet.write(row, col, lesson.name)
        col += 1
    row += 1
    col = 0
    for student in group.student_set.all():
        sheet.write(row, col, student.name)
        col += 1
        for attendance in student.attendance_set.filter(lesson__subject_id=subject.id):
            sheet.write(row, col, attendance.visit)
            col += 1
        row += 1
        col = 0

    sheet.write(row, col, "Результаты")
    row += 1
    sheet.write(row, col, "Студент")
    col += 1
    for task in subject.task_set.all():
        sheet.write(row, col, task.name)
        col += 1
    row += 1
    col = 0
    for student in group.student_set.all():
        sheet.write(row, col, student.name)
        col += 1
        for result in student.result_set.filter(task__subject_id=subject.id):
            sheet.write(row, col, result.rating)
            col += 1
        row += 1
        col = 0

    path = "groups/static/docs/spreadsheet-" + str(group.id) + "-" + str(subject.id) + ".xlsx"
    book.save(path)
    return path


def create_xls(request, pk, id):
    group = Group.objects.get(id=pk)
    subject = group.subjects.get(id=id)
    path = create_xls_(group, subject)
    file = open(path, 'rb')
    response = HttpResponse(file, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=table.xlsx'
    return response


def sending(request, pk, id):
    group = Group.objects.get(id=pk)
    students = group.student_set.all()
    emails = [student.email for student in students]
    email = EmailMessage(
        'Результаты',
        'Здравствуй, вот ваша успеваемость',
        settings.EMAIL_HOST_USER,
        emails
    )
    path = create_xls_(group, Subject.objects.get(id=id))
    email.attach_file(path)
    email.send()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
