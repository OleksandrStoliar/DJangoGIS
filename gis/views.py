# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from gis.models import Articles

# Create your views here.
def home(request):

    # return HttpResponse("Hello world")
    #return render(request, 'gis/home.html')
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'gis/home.html', context)


def about(request):
    return render(request, 'gis/about.html')