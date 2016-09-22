from django.shortcuts import render

from .models import Subdivision


# from .models import LeadingInstrukciy, LeadingPolozhennya, LeadingProcedure
# from .models import DocsInstrukciy, DocsPolozhennya, DocsProcedure

def index(request):
    latest_subdivisions_list = Subdivision.objects.all()
    context = {'latest_subdivisions_list': latest_subdivisions_list}
    return render(request, 'docs/index.html', context)
