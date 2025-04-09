from django.urls import path

from customers.views import (
    CustomerProfileView,
    CustomersListView,
    CustomerUpdateView,
    ToyClubAssignView,
    ToyClubCreateView,
    ToyClubListView,
)

app_name = "customers"
urlpatterns = [
    path("list/", CustomersListView.as_view(), name="customers-list"),
    path("<int:pk>/profile/", CustomerProfileView.as_view(), name="profile"),
    path("<int:pk>/update/", CustomerUpdateView.as_view(), name="customer-update"),
    path("toyclub/create/", ToyClubCreateView.as_view(), name="toy-club-create"),
    path("toyclub/list/", ToyClubListView.as_view(), name="toy-club-list"),
    path("toyclub/<int:pk>/assign", ToyClubAssignView.as_view(), name="toy-assign"),
]
