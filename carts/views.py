from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from carts.models import Cart, CartItem
from toys.models import Toy


class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        toy = get_object_or_404(Toy, pk=pk)
        cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, toy=toy)
        if not created:
            cart_item.quantity = F("quantity") + 1
        cart_item.save()
        if request.htmx:
            return render(request, "includes/part_incl/cart.html")
        return redirect(request.POST.get("next", "/"))


class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        cart_item = get_object_or_404(
            CartItem, pk=pk, cart__user=request.user, cart__is_active=True
        )
        cart_item.delete()
        return redirect("orders:order-create")
