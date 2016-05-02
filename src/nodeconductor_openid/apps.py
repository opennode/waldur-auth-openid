from django.apps import AppConfig


class NodeConductorOpenIDConfig(AppConfig):
    name = 'nodeconductor_openid'
    verbose_name = 'NodeConductor OpenID'

    def ready(self):
        pass
