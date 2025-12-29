from django.contrib import admin

from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'district', 'is_published', 'rooms', 'doctor', 
    list_display_links = 'id', 'title'
    list_editable = 'is_published', 'rooms'
    search_fields = 'title', "district", "doctor_name"
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)