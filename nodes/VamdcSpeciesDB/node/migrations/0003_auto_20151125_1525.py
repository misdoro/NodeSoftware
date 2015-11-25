# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vamdcdictatoms',
            name='abundance',
        ),
        migrations.RemoveField(
            model_name='vamdcdictatoms',
            name='element',
        ),
        migrations.RemoveField(
            model_name='vamdcdictatoms',
            name='mass',
        ),
        migrations.RemoveField(
            model_name='vamdcdictatoms',
            name='mass_reference',
        ),
        migrations.RemoveField(
            model_name='vamdcdictatoms',
            name='name',
        ),
    ]
