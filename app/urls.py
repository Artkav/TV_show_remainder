from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_information/<int:pk>/', views.add_to_list, name='add_to_list')
]
