from django.db import models
from datetime import datetime

class ExportVamdcSpeciesTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=450)
    class Meta:
        db_table = u'vamdc_species_types'

class ExportVamdcMarkupTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90)
    class Meta:
        db_table = u'vamdc_markup_types'

class ExportVamdcNodes(models.Model):
    id = models.AutoField(primary_key=True)
    short_name = models.CharField(max_length=60, blank = False)
    description = models.CharField(max_length=765, blank=True)
    contact_email = models.CharField(max_length = 100, blank = False)
    ivo_identifier = models.CharField(max_length = 100, blank = False, unique=True)

    class Meta:
        db_table = u'vamdc_nodes'

class ExportVamdcSpecies(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    inchi = models.TextField()
    inchikey = models.CharField(max_length=90)
    #inchikey_duplicate_counter = models.IntegerField()#!!!WTF, why was it unique?unique=True)
    stoichiometric_formula = models.CharField(max_length=450)#Atom symbol or molecule stoichiometric_formula
    mass_number = models.IntegerField()#atomic or molecular mass
    charge = models.IntegerField()#ion charge
    species_type = models.ForeignKey(ExportVamdcSpeciesTypes, db_column='species_type')
    #species_type = models.IntegerField(default=0, blank = False, choices=SpeciesType.SPECIES_CHOICES)
    cml = models.TextField(blank=True)
    mol = models.TextField(blank=True)#Use TextField since the mol structure size may quickly become > few kB for complex organics
    imageURL = models.CharField(max_length=765, blank=True)
    smiles = models.TextField(blank=True)
    created = models.DateTimeField(auto_now = False, editable=False, default = datetime.now)
    #status = models.IntegerField(default=RecordStatus.NEW, blank = False, choices=RecordStatus.RECORD_STATUS_CHOICES)
    #Disabled species are not exported to the public database
    origin_node = models.ForeignKey(ExportVamdcNodes, db_column='origin_node_id')
    #The source database from which this species was originally inserted.
    #A value of zero indicates that the species information was generated or acquired from a source
    #that is not one of the VAMDC member databases.
    class Meta:
        db_table = u'vamdc_species'

class ExportVamdcSpeciesNames(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.ForeignKey(ExportVamdcSpecies)
    name = models.CharField(max_length=450)
    markup_type = models.ForeignKey(ExportVamdcMarkupTypes)
    search_priority = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'vamdc_species_names'

class ExportVamdcNodeSpecies(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.ForeignKey(ExportVamdcSpecies)
    database_species_id = models.CharField(max_length=255)#, unique=True!!!!It should not be marked unique, since collisions are possible
    member_database = models.ForeignKey(ExportVamdcNodes)
    last_seen_dateTime = models.DateTimeField(auto_now = False, editable=False, default = datetime.now)
    class Meta:
        db_table = u'vamdc_node_species'