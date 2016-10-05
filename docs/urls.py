from django.conf.urls import url

from . import views

app_name = 'docs'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'(?P<subdivision_slug>\w+)/', views.InstrukciyView.as_view(), name='instr'),
]