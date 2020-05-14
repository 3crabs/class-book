from django.shortcuts import render


def save(request):
    print(1)
    print(request.path)
    return render(request, 'accouting/index.html', locals())
