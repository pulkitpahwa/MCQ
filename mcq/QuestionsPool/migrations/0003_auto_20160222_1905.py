# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SkillTest', '0001_initial'),
        ('QuestionsPool', '0002_candidate_question_pool'),
    ]

    operations = [
        migrations.AddField(
            model_name='pool',
            name='skill_test',
            field=models.ForeignKey(blank=True, to='SkillTest.Skill_test', null=True),
        ),
        migrations.AlterField(
            model_name='pool',
            name='contest',
            field=models.ForeignKey(blank=True, to='contest.Contest', null=True),
        ),
    ]
