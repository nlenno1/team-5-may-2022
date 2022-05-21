from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('send', views.send_connection_request, name='send_connection_request'),
]
