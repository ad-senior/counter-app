from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient


class CounterAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_get_count(self):
        res = self.client.get('/api/counter/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(type(res.data.get('value')), int)

    def test_decrease_count(self):
        res = self.client.get('/api/counter/')
        previous_count = res.data.get('value')

        res = self.client.post('/api/counter/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        new_count = res.data.get('value')

        self.assertNotEqual(previous_count, new_count)
        self.assertEqual(previous_count - 1, new_count)

    def test_reset_count(self):
        res = self.client.post('/api/counter/reset/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data.get('value'), 2)
