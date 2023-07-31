from django.urls import path
from . import views

urlpatterns = [
    path('', views.stories, name='stories'),
    path('<int:story_id>/', views.story_detail, name='story_detail'),
]
