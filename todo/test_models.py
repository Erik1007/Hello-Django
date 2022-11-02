from django.test import TestCase
from .models import Item


# Create your tests here.
class TestModels(TestCase):

    def test_defaults_to_false(self):
        item = Item.object.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.object.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
