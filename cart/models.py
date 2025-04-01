from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from toys.models import Toy


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    order_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cart_items"
    )
    toy = models.ForeignKey(
        Toy, on_delete=models.CASCADE, related_name="toys_in_cart"
    )
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total_price = self.toy.price * self.quantity
        super().save(*args, **kwargs)
