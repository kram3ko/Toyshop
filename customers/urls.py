from django.urls import path

from customers.views import ProfileUserView

app_name = "customers"
urlpatterns = [
    path("", ProfileUserView.as_view(), name="customers"),
]
