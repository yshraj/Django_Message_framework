from django.contrib import admin
from django.urls import path
from app.views import index, show_messages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('show_messages/', show_messages),
]
