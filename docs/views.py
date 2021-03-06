from django.views import generic
from docs import apps
from django.shortcuts import get_object_or_404

from .models import Subdivision, Leading, DocsLeading

class IndexView(generic.ListView):
    template_name = 'docs/category_list.html'
    context_object_name = 'latest_subdivisions_list'
    queryset = Subdivision.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        app_docs = apps.InstrConfig.verbose_name
        context['app_docs'] = app_docs
        return context

class LeadingView(generic.DetailView):
    template_name = 'docs/documents.html'
    model = Leading
    context_object_name = 'leading_detail'

    def get_context_data(self, **kwargs):
        context = super(LeadingView, self).get_context_data(**kwargs)
        #        context['subdivision'] = self.subdivision.get().title
        context['leading_slug'] = self.request.path.split('/')[-1]
        return context

class SubdivisionView(generic.ListView):
    model = Subdivision
    template_name = 'docs/documents_list.html'
    context_object_name = 'instr'

    # def get_queryset(self):
    #     sdivision = Subdivision.objects.filter(slug=self.request.path.split('/')[-2])

    def get_context_data(self, **kwargs):
        context = super(SubdivisionView, self).get_context_data(**kwargs)
#        context['subdivision'] = self.subdivision.get().title
        context['subdivision_slug'] = self.request.path.split('/')[-1]
        context['subdivision_title'] = Subdivision.objects.filter(slug=self.request.path.split('/')[-1]).get()
        # context['subdivision'] = Subdivision.objects.select_related().get(slug=self.request.path.split('/')[-2])
        app_docs = apps.InstrConfig.verbose_name
        context['app_docs'] = app_docs
        # context['latest_instr_list'] = Leading.objects.filter(doc_type_choices='INSTR').filter(subdivision = self.subdivision)
        # context['latest_instr_list'] = Leading.objects.filter(doc_type_choices='INSTR')
        context['latest_instr_list'] = Leading.objects.filter(doc_type_choices='INSTR').filter(subdivision=Subdivision.objects.filter(slug=self.request.path.split('/')[-1]))
        context['latest_pol_list'] = Leading.objects.filter(doc_type_choices='POL').filter(subdivision=Subdivision.objects.filter(slug=self.request.path.split('/')[-1]))
        context['latest_proc_list'] = Leading.objects.filter(doc_type_choices='PROC').filter(subdivision=Subdivision.objects.filter(slug=self.request.path.split('/')[-1]))
        return context
