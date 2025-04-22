from django.conf import settings
from django.db import models

from toys.models import Toy


class WishList(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wishlists",
    )
    toys = models.ManyToManyField(Toy, through="WishListItem", related_name="wishlist")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Wish List"

class WishListItem(models.Model):
    wishlist = models.ForeignKey(
        WishList, on_delete=models.CASCADE, related_name="items"
    )
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE, related_name="wish_list")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.toy.name} - {self.quantity} pcs"
