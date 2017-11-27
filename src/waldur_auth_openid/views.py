from __future__ import unicode_literals

import six
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from nodeconductor.core.views import RefreshTokenMixin

from .log import event_logger


@login_required
def login_complete(request):
    """
    Callback view called after user has successfully logged in.
    Redirects user agent to frontend view with valid token as hash parameter.
    """
    token = RefreshTokenMixin().refresh_token(request.user)
    url_template = settings.WALDUR_AUTH_OPENID['LOGIN_URL_TEMPLATE']
    url = url_template.format(token=token.key)
    event_logger.auth_openid.info(
        'User {user_full_name} authenticated successfully with eID.',
        event_type='auth_logged_in_with_openid',
        event_context={'user': request.user}
    )
    return HttpResponseRedirect(url)


def login_failed(request, message):
    url_template = settings.WALDUR_AUTH_OPENID['LOGIN_FAILED_URL_TEMPLATE']
    params = six.moves.urllib.parse.urlencode(dict(message=message))
    url = '%s?%s' % (url_template, params)
    return HttpResponseRedirect(url)
