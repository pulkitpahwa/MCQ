# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('SkillTest', '0001_initial'),
        ('contest', '0002_contest_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Questions', '0004_auto_20160222_1230'),
        ('QuestionsPool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate_Question_pool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidate', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('contest', models.ForeignKey(blank=True, to='contest.Contest', null=True)),
                ('question', models.ForeignKey(to='Questions.Question')),
                ('skill_test', models.ForeignKey(to='SkillTest.Skill_test')),
            ],
        ),
    ]
