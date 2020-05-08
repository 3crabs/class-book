from django.shortcuts import render

from models.subject import Subject


def index(request):
    subjects = [
        Subject(1, "Математика"),
        Subject(2, "Физика"),
        Subject(3, "Химия"),
    ]
    return render(request, "subjects/index.html", {'subjects': subjects})
