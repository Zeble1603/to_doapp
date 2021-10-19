from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class LoginTest(TestCase):

    # We test the login process, the user creation, and the login page

    @classmethod
    def setUp(self):
        self.credentials = {
                'username': 'CristoCanyon',
                'password': 'Lastman'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post(reverse("accounts:login"),self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)    

    

