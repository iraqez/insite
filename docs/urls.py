from django.conf.urls import url


from . import views
from docs.views import SubdivisionView, LeadingView

app_name = 'docs'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(?P<subdivision_slug>)/$', SubdivisionView.as_view(), name='instr'),
    url(r'^(?P<subdivision_slug>)/(?P<slug>)/', LeadingView, name='leading_detail'),
   # url(r'viddil-personalu/poryadok-prijnyattya-na-robotu/', LeadingView.as_view, name='leading_detail'),
    # url(r'^test/', LeadingView.as_view, name='docs'),
]