from django.urls import include, path

from accounts.views import ActivateAccountView, CustomerSignUpView

app_name = "accounts"

urlpatterns = [
    path("signup/", CustomerSignUpView.as_view(), name="signup"),
    path("activate/<uidb64>/<token>/", ActivateAccountView.as_view(), name="activate"),
    path("", include("django.contrib.auth.urls")),
]
