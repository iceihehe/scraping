# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fetchcar', '0008_auto_20150324_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='url',
        ),
    ]
