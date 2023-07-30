from django.test import TestCase
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="Tomato Pasta", price=7.99, inventory=30)
        Menu.objects.create(title="Bruschetta", price=5.99, inventory=30)
        Menu.objects.create(title="Tiramisu", price=4.99, inventory=30)
        Menu.objects.create(title="Greek Salad", price=5.99, inventory=30)
        Menu.objects.create(title="Strawberry Cheesecake", price=4.99, inventory=30)

    def test_get_all(self):
        self.setup()
        expected_items = ['Tomato Pasta : 7.99',
                          'Bruschetta : 5.99',
                          'Tiramisu : 4.99',
                          'Greek Salad : 5.99',
                          'Strawberry Cheesecake : 4.99',]
        menu_items = Menu.objects.all()
        received_expected_items = []
        received_unexpected_items = []
        for item in menu_items:
            if(str(item) in expected_items):
                #print("Expected:", item)
                received_expected_items.append(item)
            else:
                #print("Unexpected:", item)
                received_unexpected_items.append(item)
        self.assertEqual(len(received_expected_items), len(expected_items))
        self.assertEqual(len(received_unexpected_items), 0)