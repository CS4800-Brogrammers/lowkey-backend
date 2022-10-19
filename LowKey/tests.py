from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductModelTestcase(TestCase):

    # Create the test object
    def setUp(self):
        Product.objects.create(product_name="Coding Stickers", price=10.00, description="Selling custom coding stickers!")

    # Grab the product price from the product that was created using its product name
    def test_get_product_price_from_product_name(self):
        product = Product.objects.get(product_name="Coding Stickers")
        self.assertEqual(product.price, 10.00)

class ProductModelTestcase2(TestCase):
    def setUp(self):
        Product.objects.create(product_name="Cookies", price=15.00, description="A dozen of your choice of cookie flavors")

    def test_price_product(self):
        product = Product.objects.get(product_name="Cookies")
        self.assertEqual(product.price, 15.00)