from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from customers.models import ToyClub

User = get_user_model()


class ToyClubViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="admin", password="pass")
        self.assignee = User.objects.create_user(username="target", password="pass")
        self.client.login(username="admin", password="pass")

    def test_toy_club_create_valid(self):
        data = {"level": "silver", "unique_number": "ABC1234567"}
        response = self.client.post(reverse("customers:toy-club-create"), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ToyClub.objects.count(), 1)
        self.assertRedirects(response, reverse("customers:toy-club-list"))

    def test_toy_club_create_invalid_length(self):
        data = {"level": "gold", "unique_number": "abc123"}
        response = self.client.post(reverse("customers:toy-club-create"), data)
        self.assertEqual(response.status_code, 200)

        errors = response.context["form"].errors["unique_number"]
        self.assertIn("Ensure this value has exactly 10 characters (it has 6).", errors)
        self.assertIn("Ensure the first characters 3 are uppercase letters.", errors)
        self.assertIn("Ensure the last 7 characters are digits.", errors)

    def test_toy_club_create_invalid_uppercase(self):
        data = {
            "level": "gold",
            "unique_number": "abc1234567",  # перші букви не великі
        }
        response = self.client.post(reverse("customers:toy-club-create"), data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Ensure the first characters 3 are uppercase letters.",
            response.context["form"].errors["unique_number"],
        )

    def test_toy_club_create_invalid_last_digits(self):
        data = {
            "level": "bronze",
            "unique_number": "ABC1234abc",  # останні не цифри
        }
        response = self.client.post(reverse("customers:toy-club-create"), data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Ensure the last 7 characters are digits.",
            response.context["form"].errors["unique_number"],
        )

    def test_toy_club_list_get_all(self):
        ToyClub.objects.create(
            unique_number="AAA1111111", level="bronze", user=self.user
        )
        ToyClub.objects.create(unique_number="BBB2222222", level="silver", user=None)
        response = self.client.get(reverse("customers:toy-club-list"))
        self.assertContains(response, "AAA1111111")
        self.assertContains(response, "BBB2222222")

    def test_toy_club_list_post_filters_unassigned(self):
        ToyClub.objects.create(
            unique_number="AAA1111111", level="bronze", user=self.user
        )
        ToyClub.objects.create(unique_number="BBB2222222", level="silver", user=None)
        response = self.client.post(
            reverse("customers:toy-club-list"), data={"club_to_user": "1"}
        )
        self.assertNotContains(response, "AAA1111111")
        self.assertContains(response, "BBB2222222")
