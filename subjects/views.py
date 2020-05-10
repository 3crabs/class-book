from django.shortcuts import render

from subjects.models import Subject


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
