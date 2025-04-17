from django.contrib import admin

from wishlists.models import WishList, WishListItem


@admin.register(WishList)
class WishlistAdmin(admin.ModelAdmin):
    pass


@admin.register(WishListItem)
class WishListItemAdmin(admin.ModelAdmin):
    pass
