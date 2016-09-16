from django.contrib import admin
from .models import Subdivision, \
                    LeadingInstrukciy, DocsInstrukciy,\
                    LeadingPolozhennya, DocsPolozhennya,\
                    LeadingProcedure, DocsProcedure


class DocsInstrukciyInLine(admin.TabularInline):
    model = DocsInstrukciy

class DocsPolozhennyaInLine(admin.TabularInline):
    model = DocsPolozhennya

class DocsProcedureInLine(admin.TabularInline):
    model = DocsProcedure

class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug' : ('title',)}

class LeadingInstrukciyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    inlines = [ DocsInstrukciyInLine ]

class LeadingPolozhennyaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    inlines = [ DocsPolozhennyaInLine ]

class LeadingProcedureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    inlines = [ DocsProcedureInLine ]

admin.site.register(Subdivision, SubdivisionAdmin)

admin.site.register(LeadingInstrukciy, LeadingInstrukciyAdmin,)
admin.site.register(LeadingPolozhennya, LeadingPolozhennyaAdmin,)
admin.site.register(LeadingProcedure, LeadingProcedureAdmin,)
