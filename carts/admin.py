from django.contrib import admin

from carts.models import CartItem, Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    fields = ["user","order_time", "is_active", "total_price"]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass
