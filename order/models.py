from django.conf import settings
from django.db import models

from cart.models import Cart


class DeliveryMethod(models.TextChoices):
    COURIER = "courier", "Courier"
    NEW_POST = "new_post", "Nova Post"
    UKR_POST = "ukr_post", "Ukr post"


class PaymentMethod(models.TextChoices):
    CARD = "card", "Card"
    CASH = "cash", "Cash"


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    cart = models.OneToOneField(
        to=Cart, on_delete=models.SET_NULL, null=True, blank=True
    )

    deliver_to = models.CharField(max_length=255)
    delivery_method = models.CharField(
        max_length=20, choices=DeliveryMethod.choices
    )
    payment_method = models.CharField(
        max_length=20, choices=PaymentMethod.choices
    )
    recipient = models.CharField(max_length=255)

    def __str__(self):
        return f"Order #{self.id} for {self.recipient}"
