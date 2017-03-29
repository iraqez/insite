from django.conf.urls import url
from django.views.generic import TemplateView

from docs.views import SubdivisionView, LeadingView, IndexView

app_name = 'docs'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
   url(r'^(?P<leading_slug>)$', LeadingView.as_view(template_name='docs/documents.html'), name='leading_detail'),
    # url(r'^test', TemplateView.as_view(template_name='docs/test.html'), name='test'),
    url(r'^(?P<subdivision_slug>)', SubdivisionView.as_view(), name='instr'),
]