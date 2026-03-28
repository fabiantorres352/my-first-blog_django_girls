from django.urls import path
from . import views # Aquí sí funciona porque views.py está en la misma carpeta

urlpatterns = [
    path('', views.post_list, name='post_list'),
]