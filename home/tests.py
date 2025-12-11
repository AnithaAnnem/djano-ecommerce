from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse

class HomeTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
