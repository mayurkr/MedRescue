# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rescue', '0006_auto_20150914_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='called_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(blank=True, max_length=30, default=''),
        ),
    ]
