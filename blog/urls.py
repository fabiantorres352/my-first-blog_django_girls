from django.urls import path
from . import views # Aquí sí funciona porque views.py está en la misma carpeta

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # Nueva ruta
]