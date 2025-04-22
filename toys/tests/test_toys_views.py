from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from toys.models import Toy, Category
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from io import BytesIO

User = get_user_model()


def generate_test_image():
    image = Image.new("RGB", (100, 100), color="blue")
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)
    return SimpleUploadedFile("test.jpg", buffer.read(), content_type="image/jpeg")


class ToyViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass")
        self.category = Category.objects.create(name="Test Category")
        self.toy = Toy.objects.create(
            name="Test Toy",
            description="Description",
            price=9999,
            stock=10,
            manufacturer="LEGO",
            owner=self.user,
        )
        self.toy.category.add(self.category)

    def test_about_view(self):
        response = self.client.get(reverse("toys:about"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        session = self.client.session
        session["last_viewed_toy"] = self.toy.id
        session.save()
        response = self.client.get(reverse("toys:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("latest_toys", response.context)
        self.assertIn("last_viewed_toy", response.context)

    def test_toy_list_view(self):
        response = self.client.get(reverse("toys:toy-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Toy")

    def test_toy_create_view_logged_in(self):
        self.client.login(username="user", password="pass")
        image = generate_test_image()
        response = self.client.post(
            reverse("toys:create-toy"),
            {
                "name": "New Toy",
                "description": "Fun",
                "price": 5555,
                "stock": 5,
                "manufacturer": "Fisher",
                "category": [self.category.id],
            },
            files={"photo": image},
        )
        self.assertEqual(Toy.objects.count(), 2)
        self.assertRedirects(
            response, reverse("toys:toy-detail", args=[Toy.objects.last().pk])
        )

    def test_toy_update_view(self):
        self.client.login(username="user", password="pass")
        response = self.client.post(
            reverse("toys:toy-update", args=[self.toy.pk]),
            {
                "name": "Updated Toy",
                "description": self.toy.description,
                "price": self.toy.price,
                "stock": self.toy.stock,
                "manufacturer": self.toy.manufacturer,
                "category": [self.category.pk],
            },
        )
        self.toy.refresh_from_db()
        self.assertEqual(self.toy.name, "Updated Toy")
        self.assertRedirects(response, reverse("toys:toy-detail", args=[self.toy.pk]))

    def test_toy_detail_view_sets_session(self):
        response = self.client.get(reverse("toys:toy-detail", args=[self.toy.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.session["last_viewed_toy"], self.toy.pk)

    def test_toy_delete_view(self):
        self.client.login(username="user", password="pass")
        response = self.client.post(reverse("toys:toy-delete", args=[self.toy.pk]))
        self.assertRedirects(response, reverse("toys:toy-list"))
        self.assertFalse(Toy.objects.filter(pk=self.toy.pk).exists())
