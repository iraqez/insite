from django.contrib import admin
from .models import Subdivision, Leading, Docs


class DocsInLine(admin.StackedInline):
    model = Docs


class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug' : ('title',)}



class LeadingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    inlines = [ DocsInLine ]

admin.site.register(Leading, LeadingAdmin,)
admin.site.register(Subdivision, SubdivisionAdmin)
