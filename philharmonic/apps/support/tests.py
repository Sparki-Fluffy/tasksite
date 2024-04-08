from django.test import TestCase


class TestSupport(TestCase):
    def test_1(self):
        response = self.client.get('/support/')
        self.assertEquals(response.status_code, 200)
