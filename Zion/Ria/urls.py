from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('product/<str:pk>/', views.product, name='product'),
    path('add_product/', views.add_product, name='add_product'),
    path('create_cart/', views.create_cart, name='create_cart'),
    path('cart_items/', views.cart_items, name='cart_items'),
    path('add_cart_item/', views.add_cart_item, name='add_cart_item'),
    path('remove_cart_item/', views.remove_cart_item, name='remove_cart_item'),
]