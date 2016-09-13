from django.shortcuts import render

from .models import Subdivision

def index(request):
    latest_subdivisions_list = Subdivision.objects.all()
    context = { 'latest_subdivisions_list': latest_subdivisions_list }
    return render(request, 'instr/index.html', context)