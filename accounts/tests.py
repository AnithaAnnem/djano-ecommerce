from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AccountsTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_register_user(self):
        response = self.client.post(reverse("register"), {
            "username": "testuser",
            "email": "test@example.com",
            "password": "Pass1234",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_login_user(self):
        User.objects.create_user(username="testuser", password="Pass1234")
        response = self.client.post(reverse("login"), {
            "username": "testuser",
            "password": "Pass1234",
        })
        self.assertEqual(response.status_code, 302)

    def test_register_view_loads(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")
