# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fetchcar', '0007_car_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='url',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
