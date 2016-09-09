from django.contrib import admin

from .models import Subdivision, Leading

class SubdivisionAdmin(Subdivision):
    fileds = ['title',]

class LeadingAdmin(Leading):
    fileds = ['subdivision', 'title', 'text', 'file']

admin.site.register(Subdivision, SubdivisionAdmin)

admin.site.register(Leading, LeadingAdmin)