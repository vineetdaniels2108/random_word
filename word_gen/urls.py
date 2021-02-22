from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('formsubmission', views.formsubmission),
    path('reset', views.reset)
    # path('display', views.display)
]