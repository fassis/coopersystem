import datetime
from django.utils import timezone

from core.tests.base import BaseTestCase as TestCase
from core.models import PENDENTE, Product, Order


class OrderTest(TestCase):
    def setUp(self):
        product = Product.objects.create(
            name="Test product name", 
            value=99.99,
            quantity=99.99,
            )

        self.order = Order.objects.create(
            product=product,
            value=11,
            quantity=22,
            requester='Requester Name',
            zip_code='Test name',
            city='Test Address',
            address='Test District',
            number=10,
        )

    def test_create(self):
        self.assertTrue(Order.objects.exists())

    def test_str(self):
        self.assertEqual('{}'.format(self.order.pk), str(self.order))

    def test_created_at(self):
        self.assertIsInstance(self.order.created_at, datetime.datetime)
    
    def test_initial_situation(self):
        self.assertEqual(PENDENTE, str(self.order.situation))