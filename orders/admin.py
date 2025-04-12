from django.contrib import admin
from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'payment_method', 'total_price', 'created_at', 'updated_at')
    search_fields = ('user__username', 'status', 'payment_method')
    list_filter = ('status', 'payment_method', 'created_at')
    readonly_fields = ('total_price', 'created_at', 'updated_at')

    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = 'Total Price'
admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'total_price')
    search_fields = ('order__id', 'product__name')
    readonly_fields = ('total_price',)
    list_filter = ('order',)

    def total_price(self, obj):
        return obj.total_price
    total_price.short_description = 'Total Price'
admin.site.register(OrderItem, OrderItemAdmin)
