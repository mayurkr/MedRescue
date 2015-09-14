# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rescue', '0003_auto_20150914_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=30, default=''),
        ),
        migrations.AlterField(
            model_name='patient',
            name='attended',
            field=models.CharField(max_length=1, choices=[('Y', 'Attended'), ('N', 'Unattended')], default='N'),
        ),
    ]
