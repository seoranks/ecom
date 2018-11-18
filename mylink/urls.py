from django.urls import path

from . import views

urlpatterns = [
    path('', views.myDisplayFunc, name='myDisplayFunc'),
]