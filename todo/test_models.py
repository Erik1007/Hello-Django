from django.test import TestCase
from .models import Item


# Create your tests here.
class TestModels(TestCase):

    def test_defaults_to_false(self):
        item = Item.object.create(name='Test Todo Item')
        self.assertFalse(item.done)
