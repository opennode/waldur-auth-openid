def save_civil_number(request, openid_response, **kwargs):
    user = request.user
    if not user.civil_number:
        user.civil_number = request.GET['openid.identity'].split(':')[2]
        user.save()
