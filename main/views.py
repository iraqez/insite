from django.shortcuts import render

from django.http import HttpResponse


def MainPageView(request):
    return HttpResponse("Это заглавная страница сайта!!!")
