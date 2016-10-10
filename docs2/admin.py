from django.contrib import admin
from .models import Subdivision, Leading, DocsLeading

class DocsInLine(admin.TabularInline):
    model = DocsLeading

class SubdivisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug' : ('title',)}

class LeadingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    list_display = ('doc_type_choices', 'title', )
    ordering = ('doc_type_choices',)
    list_filter = ('doc_type_choices', )
    inlines = [ DocsInLine ]

admin.site.register(Subdivision, SubdivisionAdmin)
admin.site.register(Leading, LeadingAdmin,)

