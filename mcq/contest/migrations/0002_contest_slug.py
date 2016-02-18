# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='slug',
            field=autoslug.fields.AutoSlugField(null=True, populate_from=b'contest_name', editable=False, blank=True, unique=True),
        ),
    ]
