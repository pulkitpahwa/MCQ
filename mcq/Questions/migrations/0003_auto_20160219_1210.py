# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0002_auto_20160219_0834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pool',
            name='contest',
        ),
        migrations.RemoveField(
            model_name='question_pool',
            name='contest',
        ),
        migrations.RemoveField(
            model_name='question_pool',
            name='pool',
        ),
        migrations.RemoveField(
            model_name='question_pool',
            name='question',
        ),
        migrations.DeleteModel(
            name='Pool',
        ),
        migrations.DeleteModel(
            name='Question_pool',
        ),
    ]
