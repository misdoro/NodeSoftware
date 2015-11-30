# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExportVamdcMarkupTypes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'vamdc_markup_types',
            },
        ),
        migrations.CreateModel(
            name='ExportVamdcNodes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('short_name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=765, blank=True)),
                ('contact_email', models.CharField(max_length=100)),
                ('ivo_identifier', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'db_table': 'vamdc_nodes',
            },
        ),
        migrations.CreateModel(
            name='ExportVamdcNodeSpecies',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('database_species_id', models.CharField(max_length=255)),
                ('last_seen_dateTime', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('member_database', models.ForeignKey(to='export.ExportVamdcNodes')),
            ],
            options={
                'db_table': 'vamdc_node_species',
            },
        ),
        migrations.CreateModel(
            name='ExportVamdcSpecies',
            fields=[
                ('id', models.CharField(max_length=120, serialize=False, primary_key=True)),
                ('inchi', models.TextField()),
                ('inchikey', models.CharField(max_length=90)),
                ('stoichiometric_formula', models.CharField(max_length=450)),
                ('mass_number', models.IntegerField()),
                ('charge', models.IntegerField()),
                ('cml', models.TextField(blank=True)),
                ('mol', models.TextField(blank=True)),
                ('imageURL', models.CharField(max_length=765, blank=True)),
                ('smiles', models.TextField(blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('origin_node', models.ForeignKey(to='export.ExportVamdcNodes', db_column=b'origin_node_id')),
            ],
            options={
                'db_table': 'vamdc_species',
            },
        ),
        migrations.CreateModel(
            name='ExportVamdcSpeciesNames',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=450)),
                ('search_priority', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('markup_type', models.ForeignKey(to='export.ExportVamdcMarkupTypes')),
                ('species', models.ForeignKey(to='export.ExportVamdcSpecies')),
            ],
            options={
                'db_table': 'vamdc_species_names',
            },
        ),
        migrations.CreateModel(
            name='ExportVamdcSpeciesTypes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=450)),
            ],
            options={
                'db_table': 'vamdc_species_types',
            },
        ),
        migrations.AddField(
            model_name='exportvamdcspecies',
            name='species_type',
            field=models.ForeignKey(to='export.ExportVamdcSpeciesTypes', db_column=b'species_type'),
        ),
        migrations.AddField(
            model_name='exportvamdcnodespecies',
            name='species',
            field=models.ForeignKey(to='export.ExportVamdcSpecies'),
        ),
    ]
