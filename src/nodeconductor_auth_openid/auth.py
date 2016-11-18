from __future__ import unicode_literals

import logging

from django.conf import settings
from django_openid_auth.auth import OpenIDBackend


logger = logging.getLogger(__name__)


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
            # Expected openid.identity value: https://openid.ee/i/EE:<personal_code>
            # Example: https://openid.ee/i/EE:37605030299
            # Only the last part (<personal_code>) is stored as civil number.
            personal_code = openid_identity.split('/')[-1].split(':')[-1]
            if personal_code.isdigit():
                user.civil_number = personal_code
            else:
                logger.warning(
                    'Unable to parse openid.identity {}: personal code is not a numeric value'.format(openid_identity))

        method_name = settings.NODECONDUCTOR_AUTH_OPENID.get('NAME', 'openid')
        user.registration_method = method_name

        user.save(update_fields=['civil_number', 'registration_method'])

        return user
