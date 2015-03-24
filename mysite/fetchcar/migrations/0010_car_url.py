# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fetchcar', '0009_remove_car_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='url',
            field=models.CharField(default='', unique=True, max_length=50),
            preserve_default=False,
        ),
    ]
