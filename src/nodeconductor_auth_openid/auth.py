from __future__ import unicode_literals

from django.conf import settings
from django_openid_auth.auth import OpenIDBackend


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
        user = super(NodeConductorOpenIDBackend, self).create_user_from_openid(openid_response)

        openid_identity = openid_response.getSigned('http://specs.openid.net/auth/2.0', 'identity')
        if openid_identity:
            # For rest-test.nodeconductor.com and api-dev.nodeconductor.com expected openid.identity is
            # https://openid.ee/i/EE:<personal_code> (example: https://openid.ee/i/EE:37605030299);
            # only the last part (EE:<personal_code>) is stored as civil number.
            user.civil_number = openid_identity.split('/')[-1]

        method_name = settings.NODECONDUCTOR_AUTH_OPENID.get('NAME', 'openid')
        user.registration_method = method_name

        user.save(update_fields=['civil_number', 'registration_method'])

        return user
