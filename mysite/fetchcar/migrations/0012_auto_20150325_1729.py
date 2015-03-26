# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fetchcar', '0011_auto_20150325_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='reg_time',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
