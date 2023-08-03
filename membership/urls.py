from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership, name='membership'),
    path('register/', views.class_register, name='class_register'),
]
