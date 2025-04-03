from django.contrib import admin

from toys.models import Toy


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ("name","price", "photo",)
