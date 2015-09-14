# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rescue', '0002_auto_20150914_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='ambulance',
            field=models.ForeignKey(null=True, to='rescue.Ambulance'),
        ),
        migrations.AddField(
            model_name='patient',
            name='called_time',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
