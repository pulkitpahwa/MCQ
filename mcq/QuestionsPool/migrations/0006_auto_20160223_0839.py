# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsPool', '0005_auto_20160223_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='skill_test',
            field=models.ForeignKey(default=1, to='SkillTest.Skill_test'),
        ),
    ]
