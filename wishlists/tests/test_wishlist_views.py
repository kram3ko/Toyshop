from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from toys.models import Toy
from wishlists.models import WishList, WishListItem

User = get_user_model()


class WishListViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass")
        self.toy = Toy.objects.create(
            name="Test Toy",
            price=100,
            stock=10,
            manufacturer="Test",
            description="Nice",
            owner=self.user,
        )
        self.client.login(username="user", password="pass")

    def test_wishlist_detail_view_creates_wishlist(self):
        response = self.client.get(reverse("wishlists:wishlist-detail"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(WishList.objects.filter(user=self.user).exists())

    def test_add_to_wishlist_creates_item(self):
        response = self.client.post(
            reverse("assign-wishlist", args=[self.toy.pk])
        )
        self.assertEqual(WishListItem.objects.count(), 1)
        item = WishListItem.objects.first()
        self.assertEqual(item.toy, self.toy)
        self.assertEqual(item.quantity, 1)

    def test_add_to_wishlist_increments_quantity(self):
        wishlist = WishList.objects.create(user=self.user)
        WishListItem.objects.create(wishlist=wishlist, toy=self.toy, quantity=1)
        self.client.post(reverse("assign-wishlist", args=[self.toy.pk]))
        item = WishListItem.objects.get(wishlist=wishlist, toy=self.toy)
        item.refresh_from_db()
        self.assertEqual(item.quantity, 2)

    def test_remove_from_wishlist(self):
        wishlist = WishList.objects.create(user=self.user)
        item = WishListItem.objects.create(wishlist=wishlist, toy=self.toy)
        response = self.client.post(
            reverse("wishlists:remove-from-wishlist", args=[item.pk])
        )
        self.assertFalse(WishListItem.objects.filter(pk=item.pk).exists())

    def test_detail_view_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse("wishlists:wishlist-detail"))
        self.assertNotEqual(response.status_code, 200)
