from django.contrib import admin
from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'created_at', 'updated_at')
    search_fields = ('user__username',)
    readonly_fields = ('total_price', 'created_at', 'updated_at')

    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = 'Total Price'
admin.site.register(Cart, CartAdmin)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'total_price_display')
    list_filter = ('cart', 'product')
    search_fields = ('product__name', 'cart__user__username')
    ordering = ('-id',)

    def total_price_display(self, obj):
        return obj.total_price
    total_price_display.short_description = "Total Price"
