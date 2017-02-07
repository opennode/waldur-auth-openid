from . import utils


# Civil number should be updated after each login because it can be changed or
# defined for user.
def save_civil_number(request, openid_response, **kwargs):
    if 'openid.identity' not in request.GET:
        return
    user = request.user
    civil_number = utils.get_civil_number(request.GET['openid.identity'])
    if user.civil_number != civil_number:
        user.civil_number = civil_number
        user.save()
