# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SkillTest', '0002_skill_test_contest'),
        ('QuestionsPool', '0004_auto_20160223_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_pool',
            name='skill_test',
            field=models.ForeignKey(default=1, to='SkillTest.Skill_test'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question_pool',
            name='contest',
            field=models.ForeignKey(blank=True, to='contest.Contest', null=True),
        ),
    ]
