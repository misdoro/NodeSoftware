# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0005_auto_20151125_1813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vamdcspecies',
            options={'ordering': ['mass_number', 'charge']},
        ),
        migrations.AddField(
            model_name='vamdcspeciesnames',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'New'), (1, b'Active'), (2, b'Disabled')]),
        ),
        migrations.AddField(
            model_name='vamdcspeciesstructformulae',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'New'), (1, b'Active'), (2, b'Disabled')]),
        ),
        migrations.AlterField(
            model_name='vamdcspeciesnames',
            name='markup_type',
            field=models.IntegerField(default=1, choices=[(1, b'Plain text'), (2, b'HTML'), (3, b'ReStructuredText'), (4, b'LaTeX')]),
        ),
        migrations.AlterField(
            model_name='vamdcspeciesstructformulae',
            name='markup_type',
            field=models.IntegerField(default=2, choices=[(1, b'Plain text'), (2, b'HTML'), (3, b'ReStructuredText'), (4, b'LaTeX')]),
        ),
    ]
