from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from toys.models import Toy
from carts.models import Cart, CartItem

User = get_user_model()


class CartViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="strongpassword"
        )
        self.toy = Toy.objects.create(
            owner=self.user,
            name="Test Toy",
            price=100,
            stock=10,
        )

    def test_add_to_cart_creates_cart_and_item(self):
        self.client.login(username="testuser", password="strongpassword")
        url = reverse("carts:add-to-cart", args=[self.toy.pk])

        response = self.client.post(url, {"next": "/"})

        self.assertEqual(response.status_code, 302)  # redirect
        cart = Cart.objects.get(user=self.user, is_active=True)
        item = CartItem.objects.get(cart=cart, toy=self.toy)
        self.assertEqual(item.quantity, 1)

    def test_add_to_cart_increases_quantity_if_exists(self):
        self.client.login(username="testuser", password="strongpassword")
        cart = Cart.objects.create(user=self.user, is_active=True)
        CartItem.objects.create(cart=cart, toy=self.toy, quantity=1)

        url = reverse("carts:add-to-cart", args=[self.toy.pk])
        response = self.client.post(url, {"next": "/"})

        self.assertEqual(response.status_code, 302)
        item = CartItem.objects.get(cart=cart, toy=self.toy)
        self.assertEqual(item.quantity, 2)

    def test_remove_from_cart_deletes_item(self):
        self.client.login(username="testuser", password="strongpassword")
        cart = Cart.objects.create(user=self.user, is_active=True)
        item = CartItem.objects.create(cart=cart, toy=self.toy, quantity=1)

        url = reverse("carts:remove-from-cart", args=[item.pk])
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(CartItem.objects.filter(pk=item.pk).exists())
