from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('main.urls')),
    url(r'^docs2/', include('docs2.urls')),


    url(r'^admin/', admin.site.urls),
]
