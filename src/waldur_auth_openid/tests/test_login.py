from django.test import TestCase
from rest_framework import status

from waldur_core.core.tests.helpers import override_waldur_core_settings
from ..views import login_failed


class LoginTest(TestCase):
    def test_when_login_failed_user_is_redirected_to_frontend_with_message_as_query_param(self):
        error_message = 'Disabled account'
        expected_url = 'http://example.com/#/login_failed/?message=Disabled+account'

        with override_waldur_core_settings(LOGIN_FAILED_URL='http://example.com/#/login_failed/'):
            response = login_failed(None, error_message)
            self.assertEqual(response.status_code, status.HTTP_302_FOUND)
            self.assertEqual(response['Location'], expected_url)
