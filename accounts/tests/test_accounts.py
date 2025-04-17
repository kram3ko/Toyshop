from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from accounts.services.token_service import account_activation_token

User = get_user_model()


class CustomerSignUpViewTests(TestCase):
    def setUp(self):
        self.signup_url = reverse("accounts:signup")

    @patch("accounts.services.email_service.EmailMessage.send")
    def test_user_created_as_inactive_and_email_sent(self, mock_send_email):
        response = self.client.post(
            self.signup_url,
            {
                "username": "testuser",
                "password1": "TestPassword123!",
                "password2": "TestPassword123!",
                "first_name": "John",
                "last_name": "Doe",
                "email": "john@example.com",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/email_confirmation_sent.html")

        user = User.objects.get(username="testuser")
        self.assertFalse(user.is_active)
        mock_send_email.assert_called_once()


class ActivateAccountViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="inactiveuser", password="TestPassword123!", is_active=False
        )

    def test_activation_with_valid_token(self):
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = account_activation_token.make_token(self.user)
        activation_url = reverse(
            "accounts:activate", kwargs={"uidb64": uid, "token": token}
        )

        response = self.client.get(activation_url)

        self.user.refresh_from_db()
        self.assertTrue(self.user.is_active)
        self.assertRedirects(response, reverse("accounts:login"))
