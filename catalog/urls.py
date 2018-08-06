from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.temples, name='temples'),
    path('', views.gods, name='gods'),
    ]
