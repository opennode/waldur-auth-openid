# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import migrations


def update_usernames(apps, schema_editor):
    User = get_user_model()
    registration_method = settings.NODECONDUCTOR_AUTH_OPENID.get('NAME', 'openid')
    for user in User.objects.filter(registration_method=registration_method).iterator():
        user.username = uuid.uuid4().hex[:30]
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('nodeconductor_auth_openid', '0001_update_nicknames'),
    ]

    operations = [
            migrations.RunPython(update_usernames),
    ]
