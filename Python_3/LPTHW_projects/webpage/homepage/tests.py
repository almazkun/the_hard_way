from django.test import TestCase
from django.urls import reverse


class TestGreeting(TestCase):
    def test_greeting_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter")
