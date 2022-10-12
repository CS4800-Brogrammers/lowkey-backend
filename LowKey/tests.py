from django.test import TestCase

# Create your tests here.
class ViewsTest(TestCase):
    def test_alfred_url(self):
        response = self.client.get("/alfred/")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"text": "Hi this is Alfred"})