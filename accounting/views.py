from django.http import HttpResponseRedirect

from accounting.models import Attendance, Result


def save_rating(request, pk):
    result = Result.objects.get(id=pk)
    result.date = request.POST['date']
    result.rating = request.POST['rating']
    result.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def save_visit(request, pk):
    if 'visit' in request.POST:
        visit = bool(request.POST['visit'])
    else:
        visit = False
    attendance = Attendance.objects.get(id=pk)
    attendance.visit = visit
    attendance.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
