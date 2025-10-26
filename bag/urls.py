from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_bag, name='shopping_bag'),
    path('add/<item_id>/', views.add_to_bag, name="add_to_bag"),
    path('adjust/<item_id>/', views.adjust_qty, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]