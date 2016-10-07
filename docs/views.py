from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Subdivision
from .models import LeadingInstrukciy, LeadingPolozhennya, LeadingProcedure
# from .models import DocsInstrukciy, DocsPolozhennya, DocsProcedure

class IndexView(generic.ListView):
    template_name = 'docs/category_list.html'
    context_object_name = 'latest_subdivisions_list'
    queryset = Subdivision.objects.all()

# class InstrukciyView(generic.ListView):
#     template_name = 'docs/documents_list.html'
#     context_object_name = 'latest_instr_list'
#     queryset = LeadingInstrukciy.objects.filter(subdivision__leadinginstrukciy__slug='instrukciya-dlya-it')

class SubdivisionInstrView(generic.ListView):
    template_name = 'docs/documents_list.html'
    context_object_name = 'latest_instr_list'

    def get_queryset(self):
        self.subdivision = Subdivision.objects.filter(slug=self.request.path.split('/')[-2])
        return LeadingInstrukciy.objects.filter(subdivision=self.subdivision)

    def get_context_data(self, **kwargs):
        context = super(SubdivisionInstrView, self).get_context_data(**kwargs)
        context['subdivision'] = self.subdivision.get()
        return context



