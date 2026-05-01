from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('saludo/<str:nombre>/', views.saludo, name='saludo'),
]
