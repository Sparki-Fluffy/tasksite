from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def news(request):
    return render(request, 'main/news.html')


def support(request):
    return render(request, 'main/support.html')


def reservation(request):
    return render(request, 'main/reservation.html')


def schedule(request):
    return render(request, 'main/schedule.html')