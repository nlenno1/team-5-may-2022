from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('send', views.send_connection_request, name='send_connection_request'),
    path('search', views.connection_request_search, name='connection_request_search'),
]
