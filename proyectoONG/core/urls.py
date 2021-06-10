from django.contrib import admin
from django.urls import path
from .views import coraje, doraemon, garfield, gatos, index, patan, perros, scooby, tom

urlpatterns = [
    path('', index, name='index'),
    path('gatos/', gatos, name='gatos'),
    path('perros/', perros, name='perros'),
    path('doraemon/', doraemon, name='doraemon'),
    path('tom/', tom, name='tom'),
    path('garfield/', garfield, name='garfield'),
    path('scooby/', scooby, name='scooby'),
    path('patan/', patan, name='patan'),
    path('coraje/', coraje, name='coraje')
]