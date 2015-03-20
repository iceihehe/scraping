# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fetchcar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('brand', models.ForeignKey(to='fetchcar.Brand')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(to='fetchcar.Brand'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.ForeignKey(to='fetchcar.CarType'),
            preserve_default=True,
        ),
    ]
