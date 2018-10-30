# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from django.contrib import messages
# Create your views here.
def home (request):
    return render(request, 'user_templates/index.html')