from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('characters/', views.CharacterList.as_view(), name='characters'),
    path('menu/', views.MenuItemList.as_view(), name='menu'),
    path('products/', include('products.urls')),
    
]