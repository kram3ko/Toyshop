from django.urls import path

from customers.views import (
    CustomersListView,
    CustomerProfileView,
    CustomerRegisterView
)

app_name = "customers"
urlpatterns = [
    path("list/", CustomersListView.as_view(), name="customers-list"),
    path("<int:pk>/profile/", CustomerProfileView.as_view(), name="profile"),
    path("register/", CustomerRegisterView.as_view(), name="register"),

]
