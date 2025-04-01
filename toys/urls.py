from django.urls import path

from toys.views import HomePageView

app_name = "toys"
urlpatterns = [
    path("", HomePageView.as_view(), name="customers"),
]
