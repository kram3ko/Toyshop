from django.urls import path

from orders.views import OrderCreateView, OrderDetailView, OrderListView

app_name = "orders"

urlpatterns = [
    path("<int:pk>/detail/", OrderDetailView.as_view(), name="order-detail"),
    path("create/", OrderCreateView.as_view(), name="order-create"),
    path("", OrderListView.as_view(), name="order-list"),
]
