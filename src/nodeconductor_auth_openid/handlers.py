from . import utils


def save_civil_number(request, openid_response, **kwargs):
    if 'openid.identity' not in request.GET:
        return
    user = request.user
    civil_number = utils.get_civil_number(request.GET['openid.identity'])
    if user.civil_number != civil_number:
        user.civil_number = civil_number
        user.save()
