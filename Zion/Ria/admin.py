from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category"]
    list_filter = ["price", "name", "category"]
    search_fields = ["name", "category"]