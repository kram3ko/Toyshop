from carts.models import Cart
from toys.models import Category


def cart_item_count(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, is_active=True).first()
        if cart:
            return {"cart_item_count": cart.cart_items.count()}
    return {"cart_item_count": 0}

def category_item_list(request):
    return {"categories_list": Category.objects.all()}
