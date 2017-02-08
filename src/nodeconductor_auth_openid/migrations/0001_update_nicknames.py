# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import migrations


def update_usernames(apps, schema_editor):
    User = get_user_model()
    registration_method = settings.NODECONDUCTOR_AUTH_OPENID.get('NAME', 'openid')
    for user in User.objects.filter(registration_method=registration_method).iterator():
        user.username = user.username.replace(' ', '')
        user.save()


class Migration(migrations.Migration):

    operations = [
            migrations.RunPython(update_usernames),
    ]
