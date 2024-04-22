from django.contrib import admin
from .models import Listing
#from .models import Realtor
class ListingAdmin(admin.ModelAdmin):
  list_display = ['title','add_date']
  list_filter = ['add_date']
# Register your models here.
admin.site.register(Listing) ##pour lier model par site admin
#admin.site.register(Realtor)
