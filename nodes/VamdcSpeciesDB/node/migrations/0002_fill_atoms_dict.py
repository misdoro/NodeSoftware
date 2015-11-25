# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from csv import reader as csv_reader
#from node.models import VamdcDictAtoms

class Migration(migrations.Migration):

    def bulkaddatoms(apps, schema_editor):
      VamdcDictAtoms= apps.get_model("node", "VamdcDictAtoms")
      
      with open('node/migrations/nuclei.csv') as csvfile:
        csvreader = csv_reader(csvfile)
        csvreader.next()#Ignore header row
        for row in csvreader:
          VamdcDictAtoms.objects.create(
            symbol=row[1],
            mass_number=row[2],
            most_abundant=row[3],
            nuclear_charge=row[4],
            ).save()

    dependencies = [
      ('node', '0001_initial'),
      ('node', '0003_auto_20151125_1525'),
    ]

    operations = [
      migrations.RunPython(bulkaddatoms),
    ]


    