from django.contrib import admin
#from django.contrib.admin.sites import site, AdminSite
from .models import Subdivision, Leading, Docs


# @admin.register(Subdivision, Leading,)

class DocsInLine(admin.StackedInline):
    model = Docs


class SubdivisionAdmin(admin.ModelAdmin):
    None


class LeadingAdmin(admin.ModelAdmin):
    inlines = [ DocsInLine ]
    #None

admin.site.register(Leading, LeadingAdmin)
