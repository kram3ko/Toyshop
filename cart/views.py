from django.shortcuts import get_object_or_404, redirect
from django.views import generic, View

from cart.models import Cart, CartItem
from toys.models import Toy


# Create your views here.
class AddToCartView(View):
    def post(self, request, pk, *args, **kwargs):
        toy = get_object_or_404(Toy, pk=pk)

        if not request.user.is_authenticated:
            return redirect("login")

        cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, toy=toy)
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect("toys:index")
