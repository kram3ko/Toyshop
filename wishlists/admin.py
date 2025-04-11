from django.contrib import admin

from wishlists.models import WishList, WishListItem


@admin.register(WishList)
class WishlistAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WishList._meta.fields]


@admin.register(WishListItem)
class WishListItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WishListItem._meta.fields]
