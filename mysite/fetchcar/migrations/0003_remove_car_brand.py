# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fetchcar', '0002_auto_20150320_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='brand',
        ),
    ]
