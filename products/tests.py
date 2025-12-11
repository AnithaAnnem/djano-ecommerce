from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import Product, Category

class ProductTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Shoes")
        self.product = Product.objects.create(
            title="Running Shoes",
            price=1200,
            category=self.category
        )

    def test_product_model(self):
        self.assertEqual(self.product.title, "Running Shoes")
        self.assertEqual(self.product.price, 1200)

    def test_product_list_view(self):
        response = self.client.get(reverse("product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "product/product.html")

    def test_product_detail_view(self):
        response = self.client.get(reverse("product_detail", args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
