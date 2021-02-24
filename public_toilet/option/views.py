
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def showMap(request):
    return render(request, 'option.html')

def show_chart_option(request):
    return render(request, 'select_chart_option.html')