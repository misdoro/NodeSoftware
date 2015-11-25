from django.contrib import admin

#import your models here like this:
#from DjNodeExample.node.models import *

from models import *


# add your models here to have them in the admin interface
# for example if you have a model class called "Transition":

class VamdcNodesAdmin(admin.ModelAdmin):
    def make_active(modeladmin, request, queryset):
      queryset.update(status=RecordStatus.ACTIVE)
    make_active.short_description = "Activate selected nodes"
      
    
    def make_disabled(modeladmin, request, queryset):
      queryset.update(status=RecordStatus.DISABLED)
    make_disabled.short_description = "Disable selected nodes"
    
    #make_published.short_description = "Mark selected stories as published"
    list_display = ('short_name','status','contact_email','last_update_date')
    
    actions = [make_active,make_disabled]

admin.site.register(VamdcNodes,VamdcNodesAdmin)


