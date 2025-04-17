from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Sum

from carts.models import Cart
from toys.forms import ToySearchForm
from toys.models import Category
from wishlists.models import WishList


def cart_item_count(request):
    count = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, is_active=True).first()
        if cart:
            count = cart.cart_items.aggregate(total=Sum("quantity"))["total"] or 0
    return {"cart_item_count": count}


def wishlist_item_count(request):
    count = 0
    if request.user.is_authenticated:
        try:
            wish_list = WishList.objects.get(user=request.user)
            count = wish_list.items.aggregate(total=Sum("quantity"))["total"] or 0
        except (WishList.DoesNotExist, MultipleObjectsReturned):
            pass
    return {"wishlist_item_count": count}


def category_item_list(request):
    return {"categories_list": Category.objects.all()}


def get_toy_search_form(request):
    toy = request.GET.get("toy", "")
    return {"search_form": ToySearchForm(initial={"toy": toy})}
