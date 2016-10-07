from django.conf.urls import url

from . import views
from docs.views import SubdivisionInstrView, DocView

app_name = 'docs'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(?P<subdivision_slug>\w+)/', SubdivisionInstrView.as_view(), name='instr'),
    url(r'(?P<subdivision_slug>\<slug>\w+)/', DocView.as_view(), name='doc'),
]