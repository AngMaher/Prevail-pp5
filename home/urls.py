from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('privacy_policy/', views.policy, name='privacy_policy'),
]
