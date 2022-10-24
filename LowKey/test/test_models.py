from django.test import TestCase
<<<<<<< HEAD:LowKey/tests.py
from .models import Product, Profile
=======
from LowKey.models import Product
>>>>>>> 0e2eba5eab2e3857e9df8c4d96aa46ce586bac80:LowKey/test/test_models.py

# Create your tests here.
class ProductModelTestcase(TestCase):
    """Test a sample product using the price"""
    # Create the test object
    def setUp(self):
        Product.objects.create(product_name="Coding Stickers", price=10.00, description="Selling custom coding stickers!")

    # Grab the product price from the product that was created using its product name
    def test_get_product_price_from_product_name(self):
        product = Product.objects.get(product_name="Coding Stickers")
        self.assertEqual(product.price, 10.00)

class ProductModelTestcase2(TestCase):
    """Test a 2nd product also using price"""
    def setUp(self):
        Product.objects.create(product_name="Cookies", price=15.00, description="A dozen of your choice of cookie flavors")

    def test_price_product(self):
        product = Product.objects.get(product_name="Cookies")
        self.assertEqual(product.price, 15.00)

class ProfileModelCreation(TestCase):
    """Test creation of a profile and query via the name"""
    def setUp(self):
        Profile.objects.create(name="Ketan", 
        phone_number="661-599-3660", 
        email="ketanjoshi1224@gmail.com", 
        password="password1", 
        description="Ketan's test profile")

    def obtained_profile(self):
        profile = Profile.objects.get(name="Ketan")
        self.assertEqual(Profile.name, "Ketan")