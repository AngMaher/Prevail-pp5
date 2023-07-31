from django.urls import path
from . import views

urlpatterns = [
    path('', views.classes, name='classes'),
    path('add_classes', views.add_classes, name='add_classes'),
    path('edit/<classes_id>/', views.edit_classes, name='edit_classes'),
    path('delete/<classes_id>/', views.delete_classes, name='delete_classes'),
]
