from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import get_user_model
from django_openid_auth.auth import OpenIDBackend
from django_openid_auth.exceptions import RequiredAttributeNotReturned


User = get_user_model()


class NodeConductorOpenIDBackend(OpenIDBackend):
    """ This backend sets user's full_name and email. """

    def update_user_details(self, user, details, openid_response):
        updated_fields = []

        # Don't update full_name if it is already set
        if not user.full_name:
            user.full_name = '{} {}'.format(details['first_name'], details['last_name']).strip()
            updated_fields.append('full_name')

        # Don't update email if it is already set
        if not user.email and details['email']:
            user.email = details['email']
            updated_fields.append('email')

        if updated_fields:
            user.save(update_fields=updated_fields)

    def create_user_from_openid(self, openid_response):
        details = self._extract_user_details(openid_response)
        required_attrs = getattr(settings, 'OPENID_SREG_REQUIRED_FIELDS', [])
        if getattr(settings, 'OPENID_STRICT_USERNAMES', False):
            required_attrs.append('nickname')

        for required_attr in required_attrs:
            if required_attr not in details or not details[required_attr]:
                raise RequiredAttributeNotReturned(
                    "An attribute required for logging in was not "
                    "returned ({0}).".format(required_attr))

        nickname = self._get_preferred_username(
            details['nickname'], details['email'])
        email = details['email'] or ''

        username = self._get_available_username(
            nickname, openid_response.identity_url)

        method_name = settings.NODECONDUCTOR_AUTH_OPENID.get('NAME', 'openid')
        user = User.objects.create_user(username, email, password=None, registration_method=method_name)
        self.associate_openid(user, openid_response)
        self.update_user_details(user, details, openid_response)

        return user
