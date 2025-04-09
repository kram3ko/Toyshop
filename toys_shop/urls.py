import debug_toolbar
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("", include("toys.urls", namespace="toys")),
    path("carts/", include("carts.urls", namespace="carts")),
    path("customers/", include("customers.urls", namespace="customers")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("wishlists/", include("wishlists.urls", namespace="wishlists")),
    path("__debug__/", include(debug_toolbar.urls)),
]
