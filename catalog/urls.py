from django.urls import path
from . import views


urlpatterns = [
    path('', views.TempleListView.as_view(), name='temples'),
    path('temples/', views.TempleListView.as_view(), name='temples'),
    path('temple/<str:pk>', views.TempleDetailView.as_view(), name='temple-detail'),
    path('', views.gods, name='gods'),
    ]
