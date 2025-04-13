from django.urls import path

from customers.views import (
    CustomerProfileView,
    CustomersListView,
    CustomerUpdateView,
    ToyClubAssignView,
    ToyClubCreateView,
    ToyClubListView, CustomerDeleteView, CustomerCreateView,
)

app_name = "customers"
urlpatterns = [
    path("customers/create/", CustomerCreateView.as_view(), name="customer-create"),
    path("customers/list/", CustomersListView.as_view(), name="customers-list"),
    path("customers/<int:pk>/profile/", CustomerProfileView.as_view(), name="profile"),
    path("customers/<int:pk>/update/", CustomerUpdateView.as_view(), name="customer-update"),
    path("customers/<int:pk>/delete/", CustomerDeleteView.as_view(), name="customer-delete"),
    path("toyclub/create/", ToyClubCreateView.as_view(), name="toy-club-create"),
    path("toyclub/list/", ToyClubListView.as_view(), name="toy-club-list"),
    path("toyclub/<int:pk>/assign", ToyClubAssignView.as_view(), name="toy-assign")

]
