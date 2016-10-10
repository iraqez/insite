from django.views import generic
from docs2 import apps

from .models import Subdivision, Leading

class IndexView(generic.ListView):
    template_name = 'docs2/category_list.html'
    context_object_name = 'latest_subdivisions_list'
    queryset = Subdivision.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        app_docs = apps.InstrConfig.verbose_name
        context['app_docs'] = app_docs
        return context

class SubdivisionView(generic.ListView):
    template_name = 'docs2/documents_list.html'
    # context_object_name = 'latest_instr_list'

    def get_queryset(self):
        self.subdivision = Subdivision.objects.filter(slug=self.request.path.split('/')[-2])

    def get_context_data(self, **kwargs):
        context = super(SubdivisionView, self).get_context_data(**kwargs)
        context['subdivision'] = self.subdivision.get().title
        context['subdivision_slug'] = self.request.path
        app_docs = apps.InstrConfig.verbose_name
        context['app_docs'] = app_docs
        context['latest_pol_list'] = Leading.objects.filter(doc_type_choices='POL').filter(subdivision=self.subdivision)
        context['latest_instr_list'] = Leading.objects.filter(doc_type_choices='INSTR').filter(subdivision=self.subdivision)
        context['latest_proc_list'] = Leading.objects.filter(doc_type_choices='PROC').filter(subdivision=self.subdivision)
        return context

# class LeadingView(generic.DetailView):
#     template_name = 'docs2/documents.html'
#
#     def get_queryset(self):
#         self.request
#
#     def get_slug_field(self):
#         self.slug_field