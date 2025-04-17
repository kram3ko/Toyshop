from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from carts.models import Cart
from orders.models import Order
from toys.models import Toy

User = get_user_model()


class OrderViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="buyer", password="pass")
        self.client.login(username="buyer", password="pass")
        self.cart = Cart.objects.create(user=self.user, is_active=True)
        self.toy = Toy.objects.create(
            owner=self.user,
            name="Test Toy",
            price=100,
            stock=10,
        )
        self.cart.cart_items.create(toy=self.toy, quantity=2)

    def test_order_create(self):
        response = self.client.post(
            reverse("orders:order-create"),
            data={
                "deliver_to": "My home",
                "delivery_method": "new_post",
                "payment_method": "cash",
                "recipient": "John Smith",
            },
        )
        self.assertEqual(Order.objects.count(), 1)
        order = Order.objects.first()
        self.assertEqual(order.cart, self.cart)
        expected_price = self.toy.price * 2
        self.assertEqual(order.total_price, expected_price)
        self.assertRedirects(response, order.get_absolute_url())
        self.cart.refresh_from_db()
        self.assertFalse(self.cart.is_active)

    def test_order_list_only_for_user(self):
        cart1 = Cart.objects.create(user=self.user, is_active=False)
        cart2 = Cart.objects.create(user=self.user, is_active=False)

        Order.objects.create(user=self.user, deliver_to="A", recipient="R", cart=cart1)
        Order.objects.create(user=self.user, deliver_to="B", recipient="R", cart=cart2)

        response = self.client.get(reverse("orders:order-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A")
        self.assertContains(response, "B")

    def test_order_detail_view(self):
        order = Order.objects.create(
            user=self.user, deliver_to="Z", recipient="R", cart=self.cart
        )
        response = self.client.get(reverse("orders:order-detail", args=[order.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Z")

    def test_order_detail_access_denied_for_other_user(self):
        order = Order.objects.create(
            user=self.user, deliver_to="Secret", recipient="R", cart=self.cart
        )
        other_user = User.objects.create_user(username="intruder", password="1234")
        self.client.logout()
        self.client.login(username="intruder", password="1234")
        response = self.client.get(reverse("orders:order-detail", args=[order.pk]))
        self.assertNotEqual(response.status_code, 200)
