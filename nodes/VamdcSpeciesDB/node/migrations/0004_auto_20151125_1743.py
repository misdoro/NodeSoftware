# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0003_remove_vamdcspecies_inchikey_duplicate_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vamdcspecies',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
