from django.test import TestCase
from django.test import SimpleTestCase
# Create your tests here.
from django.urls import reverse, resolve

from dashboard.views import DashboardView


class DashboardTests(SimpleTestCase):
    def setUp(self):
        url = reverse('dashboard')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'dashboard.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Dashboard')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/dashboard/')
        self.assertEqual(
            view.func.__name__,
            DashboardView.as_view().__name__
        )
