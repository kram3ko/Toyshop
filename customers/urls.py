from django.urls import path

from customers.views import CustomersListView

app_name = "customers"
urlpatterns = [
    path("", CustomersListView.as_view(), name="customers-list"),
]
