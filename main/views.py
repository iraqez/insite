from django.shortcuts import render

from django.http import HttpResponse


def MainPageView(request):
    return HttpResponse("<a href='http://in.vapg.com.ua/instrukciy/'>Посадові інструкції</a>")
