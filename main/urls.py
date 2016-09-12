from django.conf.urls import url

from main.views import MainPageView

urlpatterns = [
    url(r'^$', MainPageView, name='main'),
]