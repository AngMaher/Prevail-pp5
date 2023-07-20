from django.urls import path
from . import views

urlpatterns = [
    path('', views.success_stories, name='success_stories')
]
