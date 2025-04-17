from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.utils.datastructures import MultiValueDict

from toys.forms import ToyCreateForm, ToySearchForm
from toys.models import Category
from PIL import Image
from io import BytesIO

User = get_user_model()


def generate_test_image():
    image = Image.new("RGB", (100, 100), color="blue")
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)
    return SimpleUploadedFile("test.jpg", buffer.read(), content_type="image/jpeg")


class ToyFormTests(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Action")
        self.category2 = Category.objects.create(name="Puzzle")
        self.owner = User.objects.create_user(username="toy_owner", password="pass")

    def test_toy_create_form_valid(self):
        image = generate_test_image()
        form_data = {
            "name": "Super Toy",
            "description": "Cool toy",
            "price": 99.99,
            "stock": 10,
            "manufacturer": "LEGO",
            "category": [self.category1.pk, self.category2.pk],
        }
        files = MultiValueDict({"photo": [image]})
        form = ToyCreateForm(data=form_data, files=files)
        self.assertTrue(form.is_valid())

    def test_toy_create_form_invalid_missing_fields(self):
        form = ToyCreateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        self.assertIn("category", form.errors)

    def test_toy_search_form_valid_with_input(self):
        form = ToySearchForm(data={"toy": "Robot"})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["toy"], "Robot")

    def test_toy_search_form_valid_empty(self):
        form = ToySearchForm(data={"toy": ""})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["toy"], "")
