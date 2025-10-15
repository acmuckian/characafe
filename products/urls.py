from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_products, name='products'),
    path('wishlist/<slug:slug>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.my_wishlist, name="my_wishlist"),
    path('<slug:slug>/', views.product_detail, name="product_detail"),
]