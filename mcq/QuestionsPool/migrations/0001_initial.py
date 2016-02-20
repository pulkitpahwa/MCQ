# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_contest_slug'),
        ('Questions', '0003_auto_20160219_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tools', models.TextField(null=True, blank=True)),
                ('tools_exclusive', models.BooleanField(default=False)),
                ('pool_name', models.CharField(unique=True, max_length=50)),
                ('techniques', models.TextField(null=True, blank=True)),
                ('techniques_exclusive', models.BooleanField(default=False)),
                ('domains', models.TextField(null=True, blank=True)),
                ('domains_exclusive', models.BooleanField(default=False)),
                ('difficulty', models.TextField(null=True, blank=True)),
                ('difficulty_exclusive', models.BooleanField(default=False)),
                ('number_of_questions', models.IntegerField(default=0)),
                ('contest', models.ForeignKey(to='contest.Contest')),
            ],
        ),
        migrations.CreateModel(
            name='Question_pool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contest', models.ForeignKey(to='contest.Contest')),
                ('pool', models.ForeignKey(to='QuestionsPool.Pool')),
                ('question', models.ForeignKey(to='Questions.Question')),
            ],
        ),
    ]
