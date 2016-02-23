# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionsPool', '0003_auto_20160222_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate_question_pool',
            name='fill_ups_answer',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='candidate_question_pool',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidate_question_pool',
            name='option1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidate_question_pool',
            name='option2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidate_question_pool',
            name='option3',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidate_question_pool',
            name='option4',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidate_question_pool',
            name='option5',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidate_question_pool',
            name='option6',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidate_question_pool',
            name='score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='candidate_question_pool',
            name='time_completed',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='candidate_question_pool',
            name='time_started',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='candidate_question_pool',
            name='time_taken',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='candidate_question_pool',
            name='visited',
            field=models.BooleanField(default=False),
        ),
    ]
