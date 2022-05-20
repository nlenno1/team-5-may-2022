from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.index, name='about_us'),
    path('how-to-use', views.index, name='how_to_use'),
]
