from django_openid_auth.auth import OpenIDBackend


class NodeConductorOpenIDBackend(OpenIDBackend):
    """ This backend uses first_name and last_name to update full_name field for user. """

    def update_user_details(self, user, details, openid_response):
        super(NodeConductorOpenIDBackend, self).update_user_details(user, details, openid_response)
        user.full_name = '{} {}'.format(details['first_name'], details['last_name']).strip()
        user.save(update_fields=['full_name'])
