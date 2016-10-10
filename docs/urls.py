from django.conf.urls import url

from . import views
from docs.views import SubdivisionView, LeadingView

app_name = 'docs'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(?P<subdivision_slug>[-\w]+)/', SubdivisionView.as_view(), name='instr'),
    # url(r'^(?P<slug>[-\w]+)/', LeadingView.as_view(), name='docs'),
    url(r'^test/', LeadingView.as_view, name='docs'),
]