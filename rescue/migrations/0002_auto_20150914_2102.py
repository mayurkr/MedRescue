# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rescue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('attended', models.CharField(choices=[('Y', 'Attended'), ('N', 'Unattended')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='ambulance',
            name='available',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1),
            preserve_default=False,
        ),
    ]
