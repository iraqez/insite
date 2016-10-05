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

class InstrukciyView(generic.ListView):
    template_name = 'docs/documents_list.html'
    # context_object_name = 'latest_instr_list'
    # queryset = LeadingInstrukciy.objects.filter(subdivision__title='IT')

    def get_queryset(self):
        self.subdivision = get_object_or_404(Subdivision, name=self.args[1])
        return LeadingInstrukciy.objects.filter(subdivision=self.subdivision)

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(InstrukciyView, self).get_context_data(**kwargs)
    #     # Add in the publisher
    #     context['subdivision'] = self.sub
    #     return context


