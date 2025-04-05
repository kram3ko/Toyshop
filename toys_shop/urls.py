import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from toys_shop import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("toys/", include("toys.urls", namespace="toys")),
    path("toys/carts/", include("cart.urls", namespace="carts")),
    path("toys/customers/", include("customers.urls", namespace="customers")),
    path("toys/orders/", include("order.urls", namespace="order")),
    path("__debug__/", include(debug_toolbar.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
