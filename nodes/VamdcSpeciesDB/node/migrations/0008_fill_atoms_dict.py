# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from csv import reader as csv_reader

from json import load as json_load
from pprint import pprint
#from node.models import VamdcDictAtoms







class Migration(migrations.Migration):

    def json_load_atoms(apps,schema_editor):
        VamdcDictAtoms = apps.get_model("node", "VamdcDictAtoms")
        #JSON data from IAEA livechart https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html
        #https://www-nds.iaea.org/relnsd/zipper?name=jsondata
        with open('node/migrations/iaeaatomsjsonzipper.json') as jsonfile:
            jsondata=json_load(jsonfile)
            elementnames=jsondata['elementnames']
            elements=jsondata['elements']
            for nucleus in jsondata["nucs"]:
                charge=int(nucleus['z'])
                massnum= int(nucleus['n']) + charge
                try:
                    mass = float(nucleus['am'].split(' ')[0]) / 1e6
                except:
                    mass = float(0.)

                try:
                    hl=nucleus['h']
                except:
                    hl=''

                try:
                    abund = float(nucleus['a'].split(' ')[0])
                except:
                    abund = float(0.)
                if abund is None:
                    abund = 0.

                name=elementnames[charge]
                symbol=elements[charge]
                #Add stable and those with half life containing y, m, d or s
                if (' y ' in hl
                    or ' m 'in hl
                    or ' d ' in hl
                    or ' h ' in hl
                    or ' s ' in hl
                    or 'stable' in hl
                    ):
                    print("%s:%s:%s:%s(%s):%s:%s"%(charge,massnum,symbol,name,hl,mass,abund))
                    VamdcDictAtoms.objects.create(
                        symbol=symbol,
                        name = name,
                        nuclear_charge = charge,
                        mass_number = massnum,
                        mass = mass,
                        abundance = abund,
                        stable = 'stable' in hl,
                        most_abundant = False
                    )
                else:
                    pass


    dependencies = [
        ('node', '0007_auto_20151127_2033'),
    ]

    operations = [
        migrations.RunPython(json_load_atoms),
        migrations.RunSQL('CREATE TEMPORARY TABLE IF NOT EXISTS most_abundant as (select id,symbol,max(abundance) from vamdc_dict_atoms group by nuclear_charge order by id);'),
        migrations.RunSQL('update vamdc_dict_atoms set most_abundant=1 where id in (select id from most_abundant);'),
    ]


    