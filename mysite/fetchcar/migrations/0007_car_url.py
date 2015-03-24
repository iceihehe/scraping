# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fetchcar', '0006_auto_20150321_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='url',
            field=models.CharField(default='sdfd', unique=True, max_length=50),
            preserve_default=False,
        ),
    ]
