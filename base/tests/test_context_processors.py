from django.test import RequestFactory, TestCase
from django.contrib.auth import get_user_model

from wishlists.models import WishList, WishListItem
from base.context_processors import wishlist_context
from toys.models import Toy

User = get_user_model()


class WishlistContextTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="tester", password="1234")
        self.wishlist = WishList.objects.create(user=self.user)

        self.toy = Toy.objects.create(
            owner=self.user,
            name="Test Toy",
            price=100,
            stock=10,
        )
        WishListItem.objects.create(wishlist=self.wishlist, toy=self.toy, quantity=3)

    def test_wishlist_item_count(self):
        request = self.factory.get("/")
        request.user = self.user

        context = wishlist_context(request)
        self.assertEqual(context["wishlist_item_count"], 3)
