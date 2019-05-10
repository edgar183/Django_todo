from django.test import TestCase
from .models import Item

# Create your tests here.
class TestItemModal(TestCase):
    def test_done_defaults_to_False(self):
        item = Item(name="Test done")
        item.save()
        self.assertEqual(item.name, "Test done")
        self.assertFalse(item.done)
        
    def test_can_create_an_item_with_a_name_status(self):
        item = Item(name="Test done", done=True)
        item.save()
        self.assertEqual(item.name, "Test done")
        self.assertTrue(item.done)
        
    def test_item_a_string(self):
        item = Item(name="Test Item")
        self.assertEqual("Test Item", str(item))