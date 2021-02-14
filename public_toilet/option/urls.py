from django.urls import path

from . import views

urlpatterns = [
    path('', views.showMap, name='index')
]