# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_contest_slug'),
        ('SkillTest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill_test',
            name='contest',
            field=models.ForeignKey(blank=True, to='contest.Contest', null=True),
        ),
    ]
