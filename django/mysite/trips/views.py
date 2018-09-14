# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse


def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })
