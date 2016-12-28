from nodeconductor.core.permissions import FilteredCollaboratorsPermissionLogic


PERMISSION_LOGICS = (
    ('django_openid_auth.UserOpenID', FilteredCollaboratorsPermissionLogic(user_field='user', any_permission=True)),
)
