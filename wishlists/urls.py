from django.urls import path

from wishlists.views import (
    AssignWishListView,
    RemoveFromWishListView,
    WishListDetailView,
)

app_name = "wishlists"

urlpatterns = [
    path("wishlists/", WishListDetailView.as_view(), name="wishlist-detail"),
    path(
        "wishlists/<int:pk>/add/",
        AssignWishListView.as_view(),
        name="assign-wishlist"
    ),
    path(
        "wishlists/<int:pk>/remove",
        RemoveFromWishListView.as_view(),
        name="remove-from-wishlist",
    ),
]
