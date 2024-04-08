from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('', include('main.urls')),
    path('support/', include('support.urls')),
    path('news/', include('news.urls')),
    path('schedule/', include('schedule.urls')),
    path('reservation/', include('reservation.urls')),
]
