from django.contrib import admin
from .models import Product
from .models import Cart
from .models import CartItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category"]
    list_filter = ["price", "name", "category"]
    search_fields = ["name", "category"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "date_created", "user"]
    list_filter = ["user", "id", "date_created"]
    search_fields = ["user", "id"]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ["cart", "product", "quantity"]
    list_filter = ["product", "cart"]
    search_fields = ["cart", "product"]