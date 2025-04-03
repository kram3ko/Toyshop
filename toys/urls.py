from django.urls import path

from toys.views import HomePageView, CategoryListView, ToyListView, ToyCreateView, ToyUpdateView, ToyDetailView

app_name = "toys"
urlpatterns = [
    path("", HomePageView.as_view(), name="toys-index"),
    path("toys/categories", CategoryListView.as_view(), name="toy-category"),
    path("toys/", ToyListView.as_view(), name="toy-list"),
    path("toys/", ToyCreateView.as_view(), name="create-toy"),
    path("toys/<int:pk>/update", ToyUpdateView.as_view(), name="toy-update"),
    path("toys/<int:pk>/", ToyDetailView.as_view(), name="toy-detail")
]
