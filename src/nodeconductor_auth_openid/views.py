from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from nodeconductor.core.views import RefreshTokenMixin


@login_required
def login_complete(request):
    """
    Callback view called after user has successfully logged in.
    Redirects user agent to frontend view with valid token as hash parameter.
    """
    token = RefreshTokenMixin().refresh_token(request.user)
    url_template = settings.NODECONDUCTOR_AUTH_OPENID['LOGIN_URL_TEMPLATE']
    url = url_template.format(token=token.key)
    return HttpResponseRedirect(url)
