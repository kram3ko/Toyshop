from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from carts.models import Cart
from orders.models import Order

app_name = "orders"


class OrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    fields = "__all__"
    template_name = "toyshop/order/order_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, status = Cart.objects.get_or_create(user=self.request.user, is_active=True)
        context["carts"] = cart
        return context

    def form_valid(self, form):
        order = form.save()
        order.cart.is_active = False
        order.cart.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = "toyshop/order/order_list.html"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by("-created_at")


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "toyshop/order/order_checkout.html"
