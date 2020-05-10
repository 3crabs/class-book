from django.shortcuts import render

from groups.models import Group


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
    return render(request, 'groups/info.html', locals())
