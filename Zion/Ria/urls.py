from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('create_cart/', views.create_cart, name='create_cart'),
    path('cart_items/<uuid:cart_id>/', views.cart_items, name='cart_items'),
    path('remove_cart_item/<uuid:cart_id>/<uuid:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('<uuid:cart_id>/add_cart_item/', views.add_cart_item, name='add_cart_item'),
    path('<uuid:id>/', views.product, name='product'),
]