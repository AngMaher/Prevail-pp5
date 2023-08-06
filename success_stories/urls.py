from django.urls import path
from . import views

urlpatterns = [
    path('', views.stories, name='stories'),
    path('<int:story_id>/', views.story_detail, name='story_detail'),
    path('add_story/', views.add_story, name='add_story'),
    path('edit_story/<int:story_id>/', views.edit_story, name='edit_story'),
    path('delete/<story_id>/', views.delete_story, name='delete_story'),
]
