from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'quantity', 'in_stock', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'in_stock', 'created_at')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Product, ProductAdmin)
