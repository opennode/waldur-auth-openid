from django.test import TestCase
from rest_framework import status

from ..views import login_failed


class LoginTest(TestCase):
    def test_when_login_failed_user_is_redirected_to_frontend_with_message_as_query_param(self):
        settings = {
            'LOGIN_FAILED_URL_TEMPLATE': 'http://example.com/#/login_failed/'
        }
        error_message = 'Disabled account'
        expected_url = 'http://example.com/#/login_failed/?message=Disabled+account'

        with self.settings(NODECONDUCTOR_AUTH_OPENID=settings):
            response = login_failed(None, error_message)
            self.assertEqual(response.status_code, status.HTTP_302_FOUND)
            self.assertEqual(response['Location'], expected_url)
