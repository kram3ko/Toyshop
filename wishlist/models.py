from django.conf import settings
from django.db import models

from toys.models import Toy


class WishList(models.Model):
    title = models.CharField(max_length=65)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wishlists",
    )
    toys = models.ManyToManyField(
        "Toy", through="WishListItem", related_name="wishlists"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WishListItem(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    toy = models.ForeignKey("Toy", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["wishlist", "toy"], name="unique_toy_in_list"
            )
        ]
