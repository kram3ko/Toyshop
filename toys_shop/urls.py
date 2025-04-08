import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from toys_shop import settings

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
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
