#Initialize django
import django
import settings

from node.models import *
from export.models import *
from django.forms.models import model_to_dict


from pprint import pprint

def export_aux_tables():
    #Create the auxillary tables with the types
    print ("Populating the auxillary tables")
    labeldict={}
    labeldict['species_atom']=ExportVamdcSpeciesTypes.objects.using('export').create(**{'id':1,'name':'Atom'})
    labeldict['species_molecule']=ExportVamdcSpeciesTypes.objects.using('export').create(**{'id':2,'name':'Molecule'})

    labeldict['markup_text']= ExportVamdcMarkupTypes.objects.using('export').create(**{'id':1,'name':'Plain text'})
    labeldict['markup_html']= ExportVamdcMarkupTypes.objects.using('export').create(**{'id':2,'name':'HTML'})
    labeldict['markup_rst'] = ExportVamdcMarkupTypes.objects.using('export').create(**{'id':3,'name':'ReStructuredText'})
    labeldict['markup_tex'] = ExportVamdcMarkupTypes.objects.using('export').create(**{'id':4,'name':'LaTeX'})

    for record in labeldict.itervalues():
        record.save()

    return labeldict


def export_nodes():
    #Export active nodes
    print ("Populating the nodes table")
    exportnodes=[]
    for node in VamdcNodes.objects.using('default').filter(status=RecordStatus.ACTIVE):
        pprint(node)
        dict = model_to_dict(node, fields=[field.name for field in node._meta.fields])
        for omit_field in ['status','id']:
            dict.pop(omit_field,None)
        expnode=ExportVamdcNodes(**dict)

        exportnodes.append(expnode)
    ExportVamdcNodes.objects.using('export').bulk_create(exportnodes)

    nodedict={}
    for expnode in ExportVamdcNodes.objects.using('export').all():
        nodedict[expnode.ivo_identifier]=expnode

    return nodedict

def export_species(labeldict,nodesdict):
    print ("Populating the species table")
    exportspecies=[]
    for element in VamdcSpecies.objects.using('default').filter(status=RecordStatus.ACTIVE):
        #pprint(element)
        dict = model_to_dict(element, fields=[field.name for field in element._meta.fields])

        for omit_field in ['status','species_type','origin_member_database']:
            dict.pop(omit_field,None)

        exportelement=ExportVamdcSpecies(**dict)

        if (element.species_type==SpeciesType.ATOM):
            exportelement.species_type=labeldict['species_atom']
        else:
            exportelement.species_type=labeldict['species_molecule']

        exportelement.origin_node=nodesdict[element.origin_member_database.ivo_identifier]
        if (exportelement.origin_node is not None):
            #Sanity check to avoid errors on export
            exportspecies.append(exportelement)

    ExportVamdcSpecies.objects.using('export').bulk_create(exportspecies)


def export_species_names(labeldict):
    print ("Populating the species names")
    speciesnames=[]
    for elementName in VamdcSpeciesNames.objects.using('default').filter(status=RecordStatus.ACTIVE):
        #pprint(elementName)

        dict = model_to_dict(elementName, fields=[field.name for field in elementName._meta.fields])
        for omit_field in ['status','species','id','markup_type']:
            dict.pop(omit_field,None)

        exportName=ExportVamdcSpeciesNames(**dict)

        markup=elementName.markup_type
        if (markup==MarkupTypes.TEXT):
            exportName.markup_type=labeldict['markup_text']
        elif (markup==MarkupTypes.HTML):
            exportName.markup_type=labeldict['markup_html']
        elif (markup==MarkupTypes.RST):
            exportName.markup_type=labeldict['markup_rst']
        elif (markup==MarkupTypes.LATEX):
            exportName.markup_type=labeldict['markup_tex']

        #pprint (exportName.markup_type)

        try:
            exportName.species=ExportVamdcSpecies.objects.using('export').get(id=elementName.species.id)
            if (exportName.markup_type is not None):
                speciesnames.append(exportName)
        except:
            pass

    ExportVamdcSpeciesNames.objects.using('export').bulk_create(speciesnames)

def export_species_nodes(nodesdict):
    print ("Populating the species in nodes")
    nodespecies=[]

    for nodespec in VamdcNodeSpecies.objects.using('default').all():
        #pprint(nodespec.database_species_id)
        dict = model_to_dict(nodespec, fields=[field.name for field in nodespec._meta.fields])
        for omit_field in ['species','id','member_database']:
            dict.pop(omit_field,None)

        exportNS=ExportVamdcNodeSpecies(**dict)
        try:
            exportNS.species=ExportVamdcSpecies.objects.using('export').get(id=nodespec.species.id)
            exportNS.member_database=nodesdict[nodespec.member_database.ivo_identifier]
            nodespecies.append(exportNS)
        except:
            pass

    ExportVamdcNodeSpecies.objects.using('export').bulk_create(nodespecies)