from django.shortcuts import render

from models.group import Group


def index(request):
    groups = [
        Group(1, 'ПИ-51'),
        Group(2, 'ПИ-52'),
    ]
    return render(request, "groups/index.html", {'groups': groups})
