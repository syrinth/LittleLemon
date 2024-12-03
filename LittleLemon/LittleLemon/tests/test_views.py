from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='IceCream', price=80, inventory=100)
        Menu.objects.create(title='Pizza', price=90, inventory=80)
        Menu.objects.create(title='Steak', price=100, inventory=60)
        
    def test_getall(self):
        menu = Menu.objects.all()
        self.assertEqual(menu[0].title, "IceCream")
        self.assertEqual(menu[1].title, "Pizza")
        self.assertEqual(menu[2].title, "Steak")