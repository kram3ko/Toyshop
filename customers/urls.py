from django.urls import path

from customers.views import CustomersListView, CustomerDetailView

app_name = "customers"
urlpatterns = [
    path("list/", CustomersListView.as_view(), name="customers-list"),
    path("<int:pk>/detail/", CustomerDetailView.as_view(),name="customer-detail")
]
