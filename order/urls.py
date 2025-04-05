from django.urls import path

from order.views import OrderDetailView, OrderCreateView

app_name = "order"

urlpatterns = [
    path("<int:pk>/detail/", OrderDetailView.as_view(), name="order-detail"),
    path("create/", OrderCreateView.as_view(), name="order-create")
]
