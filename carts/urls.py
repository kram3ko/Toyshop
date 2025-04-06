from django.urls import path

from carts.views import AddToCartView

app_name = "carts"

urlpatterns = [
    path("<int:pk>/add/", AddToCartView.as_view(), name="add-to-cart"),
]
