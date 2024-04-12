from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('support/', views.support, name='support'),
    path('reservation/', views.reservation, name='reservation'),
    path('schedule/', views.schedule, name='schedule'),
]
