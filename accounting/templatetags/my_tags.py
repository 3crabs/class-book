from django import template

from groups.models import Student

register = template.Library()


@register.filter
def lessons(value, args):
    student_id = value.id
    subject_id = args.id
    student = Student.objects.get(id=student_id)
    all_count = 0
    count = 0
    for attendance in student.attendance_set.all():
        if attendance.lesson.subject.id == subject_id:
            all_count += 1
            if attendance.visit:
                count += 1
    return str(int(100 * count / all_count)) + "%"


@register.filter
def tasks(value, args):
    student_id = value.id
    subject_id = args.id
    student = Student.objects.get(id=student_id)
    all_count = 0
    s = 0
    for result in student.result_set.all():
        if result.task.subject.id == subject_id:
            all_count += 1
            s += result.rating
    return str(int(100*s/(all_count*100)))
