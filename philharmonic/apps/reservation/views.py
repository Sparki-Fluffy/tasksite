from django.shortcuts import render
from django.http import HttpResponse


def reservation(request):
    return HttpResponse('Бронирование')