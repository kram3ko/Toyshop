from django.urls import path

from toys.views import HomePageView, CategoryListView, ToyListView, ToyCreateView, ToyUpdateView, ToyDetailView

app_name = "toys"
urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("categories/", CategoryListView.as_view(), name="toy-category"),
    path("list/", ToyListView.as_view(), name="toy-list"),
    path("create/", ToyCreateView.as_view(), name="create-toy"),
    path("<int:pk>/update/", ToyUpdateView.as_view(), name="toy-update"),
    path("<int:pk>/", ToyDetailView.as_view(), name="toy-detail"),
]
