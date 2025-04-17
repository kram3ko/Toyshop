from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from carts.models import Cart
from orders.forms import OrderCreateForm
from orders.models import Order

app_name = "orders"


class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = "toyshop/order/order_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, _ = Cart.objects.get_or_create(user=self.request.user, is_active=True)
        context["cart"] = cart
        return context

    def form_valid(self, form):
        cart, _ = Cart.objects.get_or_create(user=self.request.user, is_active=True)
        form.instance.user = self.request.user
        form.instance.cart = cart
        form.instance.total_price = cart.total_price
        cart.is_active = False
        cart.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = "toyshop/order/order_list.html"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-created_at")


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Order
    template_name = "toyshop/order/order_checkout.html"

    def get_queryset(self):
        return (
            Order.objects.select_related("user", "cart")
            .prefetch_related("cart__cart_items", "cart__cart_items__toy")
            .filter(user=self.request.user)
        )
