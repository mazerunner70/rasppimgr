from django.shortcuts import render

# Create your views here.

import os
from django.http import HttpResponse
from django.template import loader

def index(request):
    name = os.environ['NAME_VAR']
    template = loader.get_template('polls/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
    # return HttpResponse(f"Hello, {name}. You're at the polls index.")
