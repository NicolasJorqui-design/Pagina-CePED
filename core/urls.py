from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('preguntas-frecuentes/', views.preguntas_frecuentes, name='preguntas_frecuentes'),
]
