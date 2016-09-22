from django.shortcuts import render

def MainPageView(request):
    return render(request, 'redirect/index.html')
