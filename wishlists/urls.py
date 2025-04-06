from django.urls import path

from wishlists.views import (
    WishListDetailView,
    AddToWishListView,
    RemoveFromWishListView
)

app_name = "wishlists"

urlpatterns = [
    path("", WishListDetailView.as_view(), name="wishlist-detail"),
    path("<int:pk>/add/", AddToWishListView.as_view(), name="add-to-wishlist"),
    path("<int:pk>/remove", RemoveFromWishListView.as_view(), name="remove-from-wishlist")
]
