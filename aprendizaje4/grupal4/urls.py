from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/', views.index, name='usuarios'),
    path('registro/', views.index, name='registro')
]