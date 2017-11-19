# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=39.99, max_digits=20, verbose_name='price'),
        ),
    ]
