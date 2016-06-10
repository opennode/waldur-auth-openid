from __future__ import unicode_literals

from nodeconductor.core import NodeConductorExtension


class NodeConductorAuthOpenIDExtension(NodeConductorExtension):
    class Settings:
        SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

        OPENID_CREATE_USERS = True
        OPENID_UPDATE_DETAILS_FROM_SREG = True
        NODECONDUCTOR_AUTH_OPENID = {
            'LOGIN_URL_TEMPLATE': 'http://example.com/#/login_complete/{token}/'
        }

    @staticmethod
    def update_settings(settings):
        settings['AUTHENTICATION_BACKENDS'] += ('django_openid_auth.auth.OpenIDBackend',)
        settings['INSTALLED_APPS'] += ('django_openid_auth',)

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
