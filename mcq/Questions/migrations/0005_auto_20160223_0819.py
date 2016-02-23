# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0004_auto_20160222_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresponse',
            name='contest',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='mcq',
        ),
        migrations.RemoveField(
            model_name='userresponse',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserResponse',
        ),
    ]
