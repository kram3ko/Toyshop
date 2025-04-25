from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from customers.models import ToyClub, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        "shop_admin",
        "join_date",
        "updated_at",
    )

    fieldsets = (
        (None, {"fields": ("password",)}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (_("Additional info"), {"fields": ("shop_admin",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "email",
                    "shop_admin",
                    "toy_club",
                ),
            },
        ),
    )
    ordering = ["email"]

@admin.register(ToyClub)
class ToyAdmin(admin.ModelAdmin):
    pass
