from django.shortcuts import render


def schedule(request):
    return render(request, 'schedule/index.html')