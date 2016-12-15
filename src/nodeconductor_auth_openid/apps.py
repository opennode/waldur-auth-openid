from django.apps import AppConfig


class NodeConductorAuthOpenIDConfig(AppConfig):
    name = 'nodeconductor_auth_openid'
    verbose_name = 'NodeConductor OpenID'

    def ready(self):
        from django_openid_auth import signals, models as auth_models
        from . import handlers

        signals.openid_login_complete.connect(
            handlers.save_civil_number,
            sender=auth_models.UserOpenID,
            dispatch_uid='nodeconductor_auth_openid.handlers.save_civil_number',
        )
