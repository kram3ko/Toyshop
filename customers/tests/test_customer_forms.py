from django.test import TestCase
from django.contrib.auth import get_user_model
from customers.forms import ToyClubCreationForm

User = get_user_model()


class ToyClubCreationFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass")

    def test_valid_data(self):
        form = ToyClubCreationForm(
            data={
                "user": self.user.pk,
                "level": "silver",
                "unique_number": "ABC1234567",
            }
        )
        self.assertTrue(form.is_valid())

    def test_invalid_length(self):
        form = ToyClubCreationForm(
            data={
                "user": self.user.pk,
                "level": "bronze",
                "unique_number": "AB1234567",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("unique_number", form.errors)

    def test_invalid_uppercase(self):
        form = ToyClubCreationForm(
            data={
                "user": self.user.pk,
                "level": "Silver",
                "unique_number": "AbC1234567",
            }
        )
        self.assertFalse(form.is_valid())

    def test_invalid_last_digits(self):
        form = ToyClubCreationForm(
            data={
                "user": self.user.pk,
                "level": "Gold",
                "unique_number": "ABC12345AA",
            }
        )
        self.assertFalse(form.is_valid())
