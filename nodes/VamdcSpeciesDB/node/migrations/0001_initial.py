# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VamdcDictAtoms',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=10)),
                ('nuclear_charge', models.IntegerField()),
                ('mass_number', models.IntegerField()),
                ('mass', models.FloatField()),
                ('abundance', models.FloatField()),
                ('stable', models.BooleanField(default=False)),
                ('most_abundant', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'vamdc_dict_atoms',
            },
        ),
        migrations.CreateModel(
            name='VamdcInchikeyExceptions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('reason', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'vamdc_inchikey_exceptions',
            },
        ),
        migrations.CreateModel(
            name='VamdcNodes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('short_name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=765, blank=True)),
                ('contact_email', models.CharField(max_length=100)),
                ('ivo_identifier', models.CharField(unique=True, max_length=100)),
                ('status', models.IntegerField(default=0, choices=[(0, b'New'), (1, b'Active'), (2, b'Disabled')])),
                ('last_update_date', models.DateTimeField(default=datetime.datetime.now, editable=False)),
            ],
            options={
                'db_table': 'vamdc_nodes',
            },
        ),
        migrations.CreateModel(
            name='VamdcNodeSpecies',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('database_species_id', models.CharField(max_length=255)),
                ('last_seen_dateTime', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('member_database', models.ForeignKey(to='node.VamdcNodes')),
            ],
            options={
                'db_table': 'vamdc_node_species',
            },
        ),
        migrations.CreateModel(
            name='VamdcSpecies',
            fields=[
                ('id', models.CharField(max_length=120, serialize=False, primary_key=True)),
                ('inchi', models.TextField()),
                ('inchikey', models.CharField(max_length=90)),
                ('stoichiometric_formula', models.CharField(max_length=450)),
                ('mass_number', models.IntegerField()),
                ('charge', models.IntegerField()),
                ('species_type', models.IntegerField(default=0, choices=[(1, b'Atom'), (2, b'Molecule')])),
                ('cml', models.TextField(blank=True)),
                ('mol', models.TextField(blank=True)),
                ('imageURL', models.CharField(max_length=765, blank=True)),
                ('smiles', models.TextField(blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('status', models.IntegerField(default=0, choices=[(0, b'New'), (1, b'Active'), (2, b'Disabled')])),
                ('origin_member_database', models.ForeignKey(to='node.VamdcNodes', db_column=b'member_databases_id')),
            ],
            options={
                'ordering': ['mass_number', 'charge'],
                'db_table': 'vamdc_species',
            },
        ),
        migrations.CreateModel(
            name='VamdcSpeciesNames',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=450)),
                ('markup_type', models.IntegerField(default=1, choices=[(1, b'Plain text'), (2, b'HTML'), (3, b'ReStructuredText'), (4, b'LaTeX')])),
                ('search_priority', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('status', models.IntegerField(default=0, choices=[(0, b'New'), (1, b'Active'), (2, b'Disabled')])),
                ('species', models.ForeignKey(to='node.VamdcSpecies')),
            ],
            options={
                'db_table': 'vamdc_species_names',
            },
        ),
        migrations.CreateModel(
            name='VamdcSpeciesStructFormulae',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('formula', models.CharField(max_length=450)),
                ('markup_type', models.IntegerField(default=2, choices=[(1, b'Plain text'), (2, b'HTML'), (3, b'ReStructuredText'), (4, b'LaTeX')])),
                ('search_priority', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('status', models.IntegerField(default=0, choices=[(0, b'New'), (1, b'Active'), (2, b'Disabled')])),
                ('species', models.ForeignKey(to='node.VamdcSpecies')),
            ],
            options={
                'db_table': 'vamdc_species_struct_formulae',
            },
        ),
        migrations.AddField(
            model_name='vamdcnodespecies',
            name='species',
            field=models.ForeignKey(to='node.VamdcSpecies'),
        ),
        migrations.AddField(
            model_name='vamdcinchikeyexceptions',
            name='species',
            field=models.ForeignKey(to='node.VamdcSpecies'),
        ),
    ]
