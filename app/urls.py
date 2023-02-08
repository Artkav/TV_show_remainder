from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add_show/', views.pars_shows, name='parse_shows'),
    path('add_information/', views.add_to_list, name='add_to_list')
]
