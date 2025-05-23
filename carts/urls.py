from django.urls import path

from carts.views import AddToCartView, RemoveFromCartView

app_name = "carts"

urlpatterns = [
    path("carts/<int:pk>/add/", AddToCartView.as_view(), name="add-to-cart"),
    path(
        "carts/<int:pk>/remove",
        RemoveFromCartView.as_view(),
        name="remove-from-cart"
    ),
]
