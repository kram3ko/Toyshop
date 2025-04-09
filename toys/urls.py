from django.urls import path

from toys.views import (
    AboutView,
    HomePageView,
    ToyCreateView,
    ToyDeleteView,
    ToyDetailView,
    ToyListView,
    ToyUpdateView,
)

app_name = "toys"
urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("list/", ToyListView.as_view(), name="toy-list"),
    path("create/", ToyCreateView.as_view(), name="create-toy"),
    path("<int:pk>/update/", ToyUpdateView.as_view(), name="toy-update"),
    path("<int:pk>/", ToyDetailView.as_view(), name="toy-detail"),
    path("<int:pk>/delete/", ToyDeleteView.as_view(), name="toy-delete"),
]
