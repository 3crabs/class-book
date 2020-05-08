from django.shortcuts import render

from groups.models import Group


def index(request):
    groups = [
        Group(1, 'ПИ-51'),
        Group(2, 'ПИ-52'),
    ]
    return render(request, "groups/index.html", {'groups': groups})
