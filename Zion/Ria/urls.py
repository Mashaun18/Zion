from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('create_cart/', views.create_cart, name='create_cart'),
    path('cart_items/', views.cart_items, name='cart_items'),
    path('<uuid:id>/add_cart_item/', views.add_cart_item, name='add_cart_item'),
    path('remove_cart_item/', views.remove_cart_item, name='remove_cart_item'),
    path('<int:id>/', views.product, name='product'),
]