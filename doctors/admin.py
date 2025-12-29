from django.contrib import admin
from .models import Doctor
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = 'name', 'email', 'is_mvp', 'hire_date'
    list_display_links = 'name', 'email'
    list_editable = 'is_mvp',
    search_fields = 'name',  
    list_per_page = 25

admin.site.register(Doctor, DoctorAdmin)    