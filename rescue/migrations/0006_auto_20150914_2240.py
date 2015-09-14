# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rescue', '0005_remove_patient_attended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ambulance',
            field=models.ForeignKey(blank=True, to='rescue.Ambulance', null=True),
        ),
    ]
