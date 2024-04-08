from django.test import TestCase


class TestNews(TestCase):
    def test_1(self):
        response = self.client.get('/news/')
        self.assertEquals(response.status_code, 200)
