# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fetchcar', '0004_auto_20150320_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.ForeignKey(to='fetchcar.CarType', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='car',
            name='city',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='car',
            name='reg_time',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
