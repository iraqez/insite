from django.contrib import admin
from .models import Subdivision, Leading, Docs


@admin.register(Subdivision, Leading, Docs)
class FileInLine(admin.TabularInline):
    model = Docs

class SubdivisionAdmin(admin.ModelAdmin):
    None


class LeadingAdmin(admin.ModelAdmin):
    inlines = [
        FileInLine,
    ]
