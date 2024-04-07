from django.contrib import admin
from .models import *


class RealtorProfileAdmin(admin.ModelAdmin):
    list_display=["profile_image","owner","name"]
    list_display_links=['owner']#pour faire link
    search_fields=["name"]#chercher a l aide user
    list_filter=["name"]
    list_editable=["name"]    
        
        
        
        
# Register your models here.
admin.site.register(RealtorProfile, RealtorProfileAdmin)
admin.site.register(CustomerProfile)