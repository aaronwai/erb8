from django.contrib import admin
from django import forms
from .models import Listing, Subject
from django.contrib.admin.widgets import FilteredSelectMultiple
from taggit.forms import TagWidget
from django.db import models
from django.forms import NumberInput
# Register your models here.
class ListingAdminForm(forms.ModelForm):
    professions= forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),        widget=FilteredSelectMultiple(verbose_name="Professions",is_stacked=False,attrs={'rows':'5'}), required=False, label="Select Professions")
    class Meta:
        model = Listing
        fields = '__all__'
        widgets = {"services": TagWidget()}
        
class ListingAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'district', 'is_published', 'rooms', 'doctor', 'tag_list', "display_professions"
    list_display_links = 'id', 'title'
    list_filter = ("doctor","services")
    list_editable = 'is_published', 'rooms'
    search_fields = 'title', "district", "doctor__name", "services__name", "professions__name"
    list_per_page = 25
    formfield_overrides = {
    models.IntegerField: {
        "widget": NumberInput(attrs = {"size": "5"})
    }
} 
    show_facets = admin.ShowFacets.ALWAYS
    def get_queryset(self,request):
        return super().get_queryset(request).prefetch_related("services", "professions")
    
    def display_professions(self,obj):
        return ", ".join([subject.name for subject in obj.professions.all()]) or "None"
    display_professions.short_description = "Professions"

class SubjectAdmin(admin.ModelAdmin):
    list_display = "name",
    search_fields = "name",
    
admin.site.register(Listing, ListingAdmin)
admin.site.register(Subject, SubjectAdmin)