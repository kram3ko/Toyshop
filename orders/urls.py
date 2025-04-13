from django.urls import path

from orders.views import OrderCreateView, OrderDetailView, OrderListView

app_name = "orders"

urlpatterns = [
    path("orders/<int:pk>/detail/", OrderDetailView.as_view(), name="order-detail"),
    path("orders/create/", OrderCreateView.as_view(), name="order-create"),
    path("orders/list", OrderListView.as_view(), name="order-list"),
]
