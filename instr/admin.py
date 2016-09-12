from django.contrib import admin
from .models import Subdivision, Leading, Docs


# @admin.register(Subdivision, Leading, Docs)

# class DocsInLine(admin.):
#     model = Docs
@admin.register(Subdivision, Leading)

class SubdivisionAdmin(admin.ModelAdmin):
    None


class LeadingAdmin(admin.ModelAdmin):
    None
    # inlines = [ DocsInLine ]
