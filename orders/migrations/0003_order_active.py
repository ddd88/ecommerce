# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-18 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_billing_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
