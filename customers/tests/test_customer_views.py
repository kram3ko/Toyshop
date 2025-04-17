from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomerUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="admin", password="pass", email="old@example.com"
        )
        self.client.login(username="admin", password="pass")

    def test_update_user_profile(self):
        response = self.client.post(
            reverse("customers:customer-update", args=[self.user.pk]),
            data={"username": "admin", "email": "new@example.com"},
        )
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, "new@example.com")


class CustomerDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="pass")
        self.client.login(username="admin", password="pass")

    def test_delete_user(self):
        response = self.client.post(
            reverse("customers:customer-delete", args=[self.user.pk])
        )
        self.assertFalse(User.objects.filter(pk=self.user.pk).exists())
        self.assertEqual(response.status_code, 302)
