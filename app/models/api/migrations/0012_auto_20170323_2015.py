# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-23 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_authenticator_auth_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticator',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]
