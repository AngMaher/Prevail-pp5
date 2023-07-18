from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('change/<item_id>/', views.change_bag, name='change_bag'),
    path('delete/<item_id>/', views.delete_from_bag, name='delete_from_bag'),
]
