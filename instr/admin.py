from django.contrib import admin
from .models import Subdivision, Leading

@admin.register(Subdivision)
@admin.register(Leading)

class SubdivisionAdmin(admin.ModelAdmin):
    fileds = ['title',]



class LeadingAdmin(admin.ModelAdmin):
    list_display = ('title', 'subdivision',)
