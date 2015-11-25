# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0002_fill_atoms_dict'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vamdcspecies',
            name='inchikey_duplicate_counter',
        ),
    ]
