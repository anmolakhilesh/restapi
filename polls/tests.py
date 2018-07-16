from django.test import TestCase

from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase, APIRequestFactory

from .views import *



class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = PollViewSet.as_view({"get":"list"})
        self.uri = '/polls/'
        self.user = self.setup_user()
        self.client = APIClient()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user("mol", email="a@a.in", password="123")

    def test_list(self):
        request = self.factory.get(self.uri)
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                            'Expected Response Code 200, received {0} instead.'
                            .format(response.status_code))

    def test_list2(self):
        self.client.login(username="mol", password="123")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_create(self):
        self.client.login(username="mol", password="123")
        params = {
            "question": "How are you?",
            "created_by": 1
            }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))
