from __future__ import unicode_literals

from nodeconductor.core import NodeConductorExtension


class NodeConductorAuthOpenIDExtension(NodeConductorExtension):
    class Settings:
        # See also: http://bazaar.launchpad.net/~django-openid-auth/django-openid-auth/trunk/view/head:/README.txt
        #AUTHENTICATION_BACKENDS += ('django_openid_auth.auth.OpenIDBackend',)  # FIXME
        LOGIN_REDIRECT_URL = '/api'
        LOGIN_URL = '/api-auth/openid/login/'
        SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


    @staticmethod
    def django_app():
        return 'nodeconductor_auth_openid'

    @staticmethod
    def django_urls():
        from .urls import urlpatterns
        return urlpatterns

    @staticmethod
    def rest_urls():
        from .urls import register_in
        return register_in
