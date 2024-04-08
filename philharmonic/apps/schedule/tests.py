from django.test import TestCase


class ScheduleTest(TestCase):
    def test_1(self):
        response = self.client.get('/schedule/')
        self.assertEquals(response.status_code, 200)
