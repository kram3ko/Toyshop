from django.conf import settings
from django.db import models

from toys.models import Toy


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="carts"
    )
    order_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    @property
    def total_price(self):
        return sum(item.total_price for item in self.cart_items.all())

    def __str__(self):
        return f"User: {self.user.email} | Total: {self.total_price} ₴"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE, related_name="toys_in_cart")
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total_price = self.toy.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.toy.name} = {self.total_price} ₴"
