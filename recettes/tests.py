from django.urls import reverse
from django.test import TestCase
import recettes

# Create your tests here.
class IndexPageTextCase(TestCase):
    def test_index_pages(self):
        response = self.client.get(reverse('recettes.index'))
        self.assertEqual(response.status_code, 200)

class ShopPageTextCase(TestCase):
    def test_shop_pages(self):
        response = self.client.get(reverse('recettes.shop'))
        self.assertEqual(response.status_code, 200)