from django.test import TestCase


class TestMain(TestCase):
    def test_1(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

