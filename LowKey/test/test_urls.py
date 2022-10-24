from django.test import SimpleTestCase
from django.urls import reverse, resolve
from LowKey.views import ben

class TestUrls(SimpleTestCase):

    def test_ben(self):
        url = reverse('ben')
        self.assertEquals(resolve(url).func, ben)