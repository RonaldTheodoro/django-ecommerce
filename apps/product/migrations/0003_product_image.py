# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='products/', verbose_name='image'),
        ),
    ]