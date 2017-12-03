from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        "Tests that home page is returned"
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        "Tests correct html for home is returned"
        request = HttpRequest()
        response = home_page(request)
        
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do Lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
