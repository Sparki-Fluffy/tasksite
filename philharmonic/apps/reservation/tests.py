from django.test import TestCase


class TestReservation(TestCase):
    def test_1(self):
        response = self.client.get('/reservation/')
        self.assertEquals(response.status_code, 200)