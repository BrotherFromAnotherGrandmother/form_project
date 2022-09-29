from django.contrib import admin
from django.urls import path
from .views import index, hello

urlpatterns = [
    path('', index),
    path('hello', hello),
]
