from django.contrib import admin
#from django.contrib.admin.sites import site, AdminSite
from .models import Subdivision, Leading, Docs


#@admin.register(Subdivision)

class DocsInLine(admin.StackedInline):
    model = Docs


class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('title', )#'slug')
    prepopulated_fields = {'slug' : ('title',)}



class LeadingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    inlines = [ DocsInLine ]
    #None

admin.site.register(Leading, LeadingAdmin,)
admin.site.register(Subdivision, SubdivisionAdmin)
