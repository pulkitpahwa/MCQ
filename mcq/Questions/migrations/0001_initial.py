# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty_tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Domain_tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option_type', models.CharField(default=b'text', max_length=5, choices=[(b'text', b'Text'), (b'image', b'Image')])),
                ('option_image', models.FileField(null=True, upload_to=b'options', blank=True)),
                ('option', models.TextField(null=True, blank=True)),
                ('is_solution', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Particpations',
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
                ('contest', models.ForeignKey(to='contest.Contest')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('description', models.TextField(null=True, blank=True)),
                ('multiple_true', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('difficulty', taggit.managers.TaggableManager(to='taggit.Tag', through='Questions.Difficulty_tags', help_text='A comma-separated list of tags.', verbose_name=b'difficulty')),
                ('domains', taggit.managers.TaggableManager(to='taggit.Tag', through='Questions.Domain_tags', help_text='A comma-separated list of tags.', verbose_name=b'domains')),
            ],
        ),
        migrations.CreateModel(
            name='Question_pool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contest', models.ForeignKey(to='contest.Contest')),
                ('pool', models.ForeignKey(to='Questions.Pool')),
                ('question', models.ForeignKey(to='Questions.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Technique_tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', models.ForeignKey(to='Questions.Question')),
                ('tag', models.ForeignKey(related_name='questions_technique_tags_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tool_tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', models.ForeignKey(to='Questions.Question')),
                ('tag', models.ForeignKey(related_name='questions_tool_tags_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='question',
            name='techniques',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='Questions.Technique_tags', help_text='A comma-separated list of tags.', verbose_name=b'techniques'),
        ),
        migrations.AddField(
            model_name='question',
            name='tools',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='Questions.Tool_tags', help_text='A comma-separated list of tags.', verbose_name=b'tools'),
        ),
        migrations.AddField(
            model_name='particpations',
            name='mcq',
            field=models.ForeignKey(to='Questions.Question'),
        ),
        migrations.AddField(
            model_name='particpations',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='options',
            name='question',
            field=models.ForeignKey(to='Questions.Question'),
        ),
        migrations.AddField(
            model_name='domain_tags',
            name='content_object',
            field=models.ForeignKey(to='Questions.Question'),
        ),
        migrations.AddField(
            model_name='domain_tags',
            name='tag',
            field=models.ForeignKey(related_name='questions_domain_tags_items', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='difficulty_tags',
            name='content_object',
            field=models.ForeignKey(to='Questions.Question'),
        ),
        migrations.AddField(
            model_name='difficulty_tags',
            name='tag',
            field=models.ForeignKey(related_name='questions_difficulty_tags_items', to='taggit.Tag'),
        ),
    ]
