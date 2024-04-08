# tests.py
from django.test import TestCase
from .models import Item


class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(
            name="Test Item", description="This is a test item.")

    def test_item_created(self):
        test_item = Item.objects.get(name="Test Item")
        self.assertEqual(test_item.description, "This is a test item.")
