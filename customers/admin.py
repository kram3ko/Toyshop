from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from customers.models import User, ToyClub


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        "shop_admin",
        "join_date",
        "updated_at",
        "toy_club",
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Additional info", {"fields": ("shop_admin","toy_club")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser",)}),
        ("Important dates", {"fields": ("last_login", "date_joined",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "first_name", "last_name", "email", "shop_admin", "toy_club"),
        }),
    )



@admin.register(ToyClub)
class ToyAdmin(admin.ModelAdmin):
    pass
