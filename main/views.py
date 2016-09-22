from django.shortcuts import render
from docs import apps

def MainPageView(request):
    app_docs = apps.InstrConfig.verbose_name
    context = {'app_docs': app_docs}
    return render(request, 'redirect/index.html', context)
