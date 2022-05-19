import datetime
from django.utils import timezone

from core.tests.base import BaseTestCase as TestCase
from core.models import DISPONIVEL, Product


class ProductTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test product name", 
            value=99.99,
            quantity=99.99,
            )

    def test_create(self):
        self.assertTrue(Product.objects.exists())

    def test_str(self):
        self.assertEqual('{}'.format(self.product.name), str(self.product))

    def test_created_at(self):
        self.assertIsInstance(self.product.created_at, datetime.datetime)
    
    def test_situation(self):
        self.assertEqual(DISPONIVEL, self.product.get_situation())