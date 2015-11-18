# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from django.contrib import admin
from datetime import datetime

class RecordStatus():
    NEW = 0
    ACTIVE = 1
    DISABLED = 2
    RECORD_STATUS_CHOICES = (
      (NEW,		'New'),
      (ACTIVE,	'Active'),
      (DISABLED,	'Disabled'))
    
class SpeciesType():
    ATOM = 1
    MOLECULE = 2
    SPECIES_CHOICES = (
      (ATOM,'Atom'),
      (MOLECULE,'Molecule'),
      )

class MarkupTypes():
    TEXT = 1
    MARKUP_TYPES = (
      (TEXT,'Plain text'),
      )

#class VamdcSpeciesTypes(models.Model):
#    id = models.AutoField(primary_key=True)
#    name = models.CharField(max_length=450)
#    class Meta:
#        db_table = u'vamdc_species_types'

class VamdcMemberDatabases(models.Model):
    id = models.AutoField(primary_key=True)
    short_name = models.CharField(max_length=60, blank = False)
    description = models.CharField(max_length=765, blank=True)
    contact_email = models.CharField(max_length = 100, blank = False)
    ivo_identifier = models.CharField(max_length = 100, blank = False, unique=True)
    status = models.IntegerField(default=0, blank = False, choices=RecordStatus.RECORD_STATUS_CHOICES)
    last_update_date = models.DateTimeField(auto_now = False, editable=False, default = datetime.now)
    class Meta:
        db_table = u'vamdc_member_databases'
        
class VamdcMemberDatabasesAdmin(admin.ModelAdmin):
    def make_active(modeladmin, request, queryset):
      queryset.update(status=RecordStatus.ACTIVE)
    make_active.short_description = "Mark selected nodes as Active"
      
    
    def make_disabled(modeladmin, request, queryset):
      queryset.update(status=RecordStatus.DISABLED)
    make_disabled.short_description = "Mark selected nodes as Disabled"
    
    #make_published.short_description = "Mark selected stories as published"
    list_display = ('short_name','status','contact_email','last_update_date')
    
    actions = [make_active,make_disabled]


class VamdcSpecies(models.Model):
    id = models.CharField(max_length=120, primary_key=True)
    inchi = models.TextField()
    inchikey = models.CharField(max_length=90)
    inchikey_duplicate_counter = models.IntegerField()#!!!WTF, why was it unique?unique=True)
    stoichiometric_formula = models.CharField(max_length=450)
    mass_number = models.IntegerField()
    charge = models.IntegerField()
    #species_type = models.ForeignKey(VamdcSpeciesTypes, db_column='species_type')
    species_type = models.IntegerField(default=0, blank = False, choices=SpeciesType.SPECIES_CHOICES)
    cml = models.CharField(max_length=765, blank=True)
    mol = models.CharField(max_length=765, blank=True)
    image = models.CharField(max_length=765, blank=True)
    smiles = models.TextField(blank=True)
    created = models.DateTimeField()
    member_database = models.ForeignKey(VamdcMemberDatabases, db_column='member_databases_id')
    class Meta:
        db_table = u'vamdc_species'

    def symbol(self):
        return self.stoichiometric_formula.replace('+','').replace('-','')

    def nuclear_charge(self):
        try:            
            ns = VamdcDictAtoms.objects.filter(element=self.symbol()).values_list('nuclear_charge',flat=True)[0]
        except IndexError:
            ns=None
        return ns

    def structural_formula(self):
        try:
            sf=self.vamdcspeciesstructformulae_set.order_by('search_priority').values_list('formula',flat=True)[0]
            # replace html-tags <sub> and <sup> with latex expressions
            # this should be improved
            sf=sf.replace("<sub>","$_{").replace("</sub>","}$").replace("<sup>","$^{").replace("</sup>","}$").replace("$$","")
        except IndexError:
            sf=""

        return sf

    def trivial_name(self):
        try:
            name=self.vamdcspeciesnames_set.order_by('search_priority').values_list('name',flat=True)[0]
            # replace html-tags <sub> and <sup> with latex expressions
            # this should be improved
            name = name.replace("<sub>","$_{").replace("</sub>","}$").replace("<sup>","$^{").replace("</sup>","}$").replace("$$","")
        except IndexError:
            name=""

        return name

    def species_foreign_ids(self):
        """
        Creates a string which is formated like a dictionary with all the foreign species ids and the related database name.
        This can be used to provide the information via a comment-elelment.
        """
        speciesids = self.vamdcmemberdatabaseidentifiers_set.all()
        return_string="{"
        for sid in speciesids:
            return_string+="{%s:%s}," % (sid.database_species_id ,sid.member_database.short_name)
        return_string += "}"

        return return_string

    def comment(self):
        """
        """
        return self.species_foreign_ids()

class VamdcConformers(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.ForeignKey(VamdcSpecies)
    conformer_name = models.CharField(max_length=450)
    class Meta:
        db_table = u'vamdc_conformers'

class VamdcInchikeyExceptions(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.ForeignKey(VamdcSpecies)
    reason = models.CharField(max_length=765)
    class Meta:
        db_table = u'vamdc_inchikey_exceptions'

#class VamdcMarkupTypes(models.Model):
#    id = models.AutoField(primary_key=True)
#    name = models.CharField(max_length=90)
#    class Meta:
#        db_table = u'vamdc_markup_types'

class VamdcMemberDatabaseIdentifiers(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.ForeignKey(VamdcSpecies)
    database_species_id = models.CharField(max_length=255, unique=True)#!!!!should it be unique?
    member_database = models.ForeignKey(VamdcMemberDatabases)
    class Meta:
        db_table = u'vamdc_member_database_identifiers'

class VamdcSpeciesNames(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.ForeignKey(VamdcSpecies)
    name = models.CharField(max_length=450)
    markup_type = models.IntegerField(default=0, blank = False, choices=MarkupTypes.MARKUP_TYPES)
    search_priority = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'vamdc_species_names'

class VamdcSpeciesResources(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.ForeignKey(VamdcSpecies)
    url = models.CharField(max_length=765)
    description = models.CharField(max_length=450)
    search_priority = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'vamdc_species_resources'

class VamdcSpeciesStructFormulae(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.ForeignKey(VamdcSpecies)
    formula = models.CharField(max_length=450)
    formula_latex = models.CharField(max_length=450)
    #markup_type = models.ForeignKey(VamdcMarkupTypes)
    markup_type = models.IntegerField(default=0, blank = False, choices=MarkupTypes.MARKUP_TYPES)
    search_priority = models.IntegerField()
    created = models.DateTimeField()
    class Meta:
        db_table = u'vamdc_species_struct_formulae'


class VamdcDictAtoms(models.Model):
    """
    This is a helper model and its contents provide
    a dictionary for atomic elements.
    !!! THIS IS NOT PART OF THE OFFICIAL VAMDC SPECIES DB !!!
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    element = models.CharField(max_length=10)
    mass_number = models.IntegerField()
    mass = models.FloatField()
    abundance = models.FloatField()
    most_abundant = models.IntegerField()
    mass_reference = models.IntegerField()
    nuclear_charge = models.IntegerField()
    class Meta:
        db_table = u'vamdc_dict_atoms'
