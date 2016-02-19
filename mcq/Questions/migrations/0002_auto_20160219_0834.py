# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='fill_ups_correct_ans',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='fill_ups_type',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'string', b'Text'), (b'int', b'Integer'), (b'float', b'Float')]),
        ),
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(default=b'choices', max_length=10, null=True, blank=True, choices=[(b'choices', b'Multiple Choices'), (b'fill_ups', b'Fill Right Answer')]),
        ),
    ]
