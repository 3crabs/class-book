from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h3>Hello, groups!</h3>")
