# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill_test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('slug', autoslug.fields.AutoSlugField(null=True, populate_from=b'name', editable=False, blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test_participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('score', models.FloatField(default=0)),
                ('participant', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('skill_test', models.ForeignKey(to='SkillTest.Skill_test')),
            ],
        ),
    ]
