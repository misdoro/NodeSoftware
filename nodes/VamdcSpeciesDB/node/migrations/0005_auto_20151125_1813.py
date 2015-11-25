# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0004_auto_20151125_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='VamdcNodeSpecies',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('database_species_id', models.CharField(max_length=255)),
                ('last_seen_dateTime', models.DateTimeField(default=datetime.datetime.now, editable=False)),
            ],
            options={
                'db_table': 'vamdc_node_species',
            },
        ),
        migrations.RenameModel(
            old_name='VamdcMemberDatabases',
            new_name='VamdcNodes',
        ),
        migrations.RemoveField(
            model_name='vamdcmemberdatabaseidentifiers',
            name='member_database',
        ),
        migrations.RemoveField(
            model_name='vamdcmemberdatabaseidentifiers',
            name='species',
        ),
        migrations.AlterModelTable(
            name='vamdcnodes',
            table='vamdc_nodes',
        ),
        migrations.DeleteModel(
            name='VamdcMemberDatabaseIdentifiers',
        ),
        migrations.AddField(
            model_name='vamdcnodespecies',
            name='member_database',
            field=models.ForeignKey(to='node.VamdcNodes'),
        ),
        migrations.AddField(
            model_name='vamdcnodespecies',
            name='species',
            field=models.ForeignKey(to='node.VamdcSpecies'),
        ),
    ]
