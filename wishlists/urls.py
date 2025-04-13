from django.urls import path

from wishlists.views import (
    AddToWishListView,
    RemoveFromWishListView,
    WishListDetailView,
)

app_name = "wishlists"

urlpatterns = [
    path("wishlists/", WishListDetailView.as_view(), name="wishlist-detail"),
    path(
        "wishlists/<int:pk>/add/",
        AddToWishListView.as_view(),
        name="add-to-wishlist"
    ),
    path(
        "wishlists/<int:pk>/remove",
        RemoveFromWishListView.as_view(),
        name="remove-from-wishlist")
]
