# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rescue', '0007_auto_20150915_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambulance',
            name='email',
            field=models.EmailField(default='driver@ambulance.com', max_length=254),
        ),
    ]
