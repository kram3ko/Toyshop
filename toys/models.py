from django.conf import settings
from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Toy(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name="toys")
    photo = ResizedImageField(
        size=[250, 250], quality=75, upload_to="toys/", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("toys:toy-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
