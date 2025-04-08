from carts.models import Cart
from toys.forms import ToySearchForm
from toys.models import Category
from wishlists.models import WishList


def cart_item_count(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, is_active=True).first()
        if cart:
            return {"cart_item_count": cart.cart_items.count()}
    return {"cart_item_count": 0}


def wishlist_item_count(request):
    if request.user.is_authenticated:
        wish_list = WishList.objects.filter(user=request.user).first()
        if wish_list:
            return {"wishlist_item_count": wish_list.items.count()}
    return {"wishlist_item_count": 0}

def get_user_status(request):
    return {"user_shop_admin" : user.shop_admin}

def category_item_list(request):
    return {"categories_list": Category.objects.all()}


def get_toy_search_form(request):
    toy = request.GET.get("toy", "")
    return {"search_form": ToySearchForm(initial={"toy": toy})}
