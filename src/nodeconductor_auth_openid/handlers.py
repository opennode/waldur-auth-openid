def save_civil_number(seder, request, openid_response, **kwargs):
    user = request.user
    if not user.civil_numer:
        user.civil_numer = request.GET['openid.identity'].split(':')[2]
        user.save()
