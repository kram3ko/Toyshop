from django.contrib.auth.models import AbstractUser
from django.db import models

from toys.models import Toy
from wishlist.models import WishList


class ToyClub(models.Model):
    class LevelChoice(models.TextChoices):
        BRONZE = "bronze", "Bronze"
        SILVER = "silver", "Silver"
        GOLD = "gold", "Gold"

    level = models.CharField(max_length=10, choices=LevelChoice.choices)
    unique_number = models.CharField(max_length=13, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    customer = models.BooleanField(default=True)
    join_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    toy_club = models.ForeignKey(
        ToyClub, on_delete=models.SET_NULL, null=True, blank=True
    )
    wish_list = models.ManyToManyField(
        Toy, through=WishList, related_name="wishers"
    )
