from __future__ import unicode_literals

import six
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django_openid_auth import views as auth_view

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


def login_failed(request, message):
    url_template = settings.NODECONDUCTOR_AUTH_OPENID['LOGIN_FAILED_URL_TEMPLATE']
    params = six.moves.urllib.parse.urlencode(dict(message=message))
    url = '%s?%s' % (url_template, params)
    return HttpResponseRedirect(url)


origin_parse_openid_response = auth_view.parse_openid_response


def _patch_request_data(request):
    """ Replace openid identity and claimed_id parameters by email-based id in request data """
    data = auth_view.get_request_data(request)
    email_id = data['openid.sreg.email'].split('@')[0]
    email_id_url = 'https://openid.ee/u/' + email_id
    _get, _post = request.GET.copy(), request.POST.copy()
    for key in ('openid.claimed_id', 'openid.identity'):
        if key in _get:
            _get[key] = email_id_url
        if key in _post:
            _post[key] = email_id_url
    request.GET = _get
    request.POST = _post


def patched_parse_openid_response(request):
    """ If request with origin data failed - try to execute it again with email-based ID """
    openid_response = origin_parse_openid_response(request)
    if not openid_response or openid_response.status != auth_view.FAILURE:
        return openid_response
    origin_identity = auth_view.get_request_data(request).get('openid.identity')
    try:
        _patch_request_data(request)
    except (KeyError, TypeError):
        # whoops, we cannot patch request properly, lets move back to the origin flow
        return openid_response
    openid_response = origin_parse_openid_response(request)
    if openid_response and openid_response.status == auth_view.SUCCESS:
        openid_response.origin_identity = origin_identity
    return openid_response


# XXX Monkey-patch parse_openid_response to perform additional query against email-based URL
auth_view.parse_openid_response = patched_parse_openid_response
