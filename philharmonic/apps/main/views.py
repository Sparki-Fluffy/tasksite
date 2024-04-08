from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, world')


def news(request):
    return HttpResponse('News page')


def support(request):
    return HttpResponse('Support page')


def schedule(request):
    return HttpResponse('Schedule page')


def reservation(request):
    return HttpResponse('Reservation page')