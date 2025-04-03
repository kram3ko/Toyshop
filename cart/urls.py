from django.urls import path

from cart.views import AddToCartView, CartDetailView

app_name = "cart"

urlpatterns = [
    path("<int:pk>/add/", AddToCartView.as_view(), name="add-to-cart"),
    path("<int:pk>detail/", CartDetailView.as_view(), name="order-detail"),

]