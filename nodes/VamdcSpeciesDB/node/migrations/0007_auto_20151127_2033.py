# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0006_auto_20151127_1905'),
    ]

    operations = [
        migrations.RunSQL('delete from vamdc_dict_atoms'),
        migrations.AddField(
            model_name='vamdcdictatoms',
            name='abundance',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vamdcdictatoms',
            name='mass',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vamdcdictatoms',
            name='name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vamdcdictatoms',
            name='stable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vamdcdictatoms',
            name='most_abundant',
            field=models.BooleanField(default=False),
        ),
    ]
