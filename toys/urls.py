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
    path("toysshop/about/", AboutView.as_view(), name="about"),
    path("toysshop/toys/list/", ToyListView.as_view(), name="toy-list"),
    path("toysshop/toys/create/", ToyCreateView.as_view(), name="create-toy"),
    path("toysshop/toys/<int:pk>/update/", ToyUpdateView.as_view(), name="toy-update"),
    path("toysshop/toys/<int:pk>/", ToyDetailView.as_view(), name="toy-detail"),
    path("toysshop/toys/<int:pk>/delete/", ToyDeleteView.as_view(), name="toy-delete"),
]
