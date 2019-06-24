# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Felicidades! Completaron la 2a evaluacion parcial")
