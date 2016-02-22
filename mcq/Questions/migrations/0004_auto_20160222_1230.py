# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0002_contest_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Questions', '0003_auto_20160219_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('time_taken', models.IntegerField(default=0)),
                ('option1', models.BooleanField(default=False)),
                ('option2', models.BooleanField(default=False)),
                ('option3', models.BooleanField(default=False)),
                ('option4', models.BooleanField(default=False)),
                ('option5', models.BooleanField(default=False)),
                ('is_correct', models.BooleanField(default=False)),
                ('score', models.FloatField(default=0)),
                ('contest', models.ForeignKey(to='contest.Contest')),
            ],
        ),
        migrations.RemoveField(
            model_name='particpations',
            name='contest',
        ),
        migrations.RemoveField(
            model_name='particpations',
            name='mcq',
        ),
        migrations.RemoveField(
            model_name='particpations',
            name='user',
        ),
        migrations.AddField(
            model_name='question',
            name='accuracy',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='avg_time',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Particpations',
        ),
        migrations.AddField(
            model_name='userresponse',
            name='mcq',
            field=models.ForeignKey(to='Questions.Question'),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
