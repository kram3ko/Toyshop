from django.urls import path

from cart.views import AddToCartView

app_name = "cart"

urlpatterns = [
    path("<int:pk>/add/", AddToCartView.as_view(), name="add-to-cart"),
]
