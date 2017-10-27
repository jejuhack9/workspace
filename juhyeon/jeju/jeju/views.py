# -*- coding: utf8 -*-

#from __future__ import unicode_literals
from elasticsearch import Elasticsearch
import numpy as np
from collections import Counter
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from jeju.forms import *
from django.contrib.auth import authenticate, login
from jeju.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from urllib.parse import unquote
import json
from ipware.ip import get_ip
from django.utils import timezone
import pytz
tz=pytz.timezone('Asia/Seoul')


def search(request):
    ip = get_ip(request)
    if request.method == 'POST':
        usr = User.objects.filter(username=request.user)
        pass

def index(request):
    context = {}
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                                password=form.cleaned_data['password1'],
                                                email=form.cleaned_data['email'],
                                                first_name=str(form.cleaned_data['rname'])+'|'+str(form.cleaned_data['phone']) + '|' + str(
                                                    form.cleaned_data['address']),
                                                last_name=form.cleaned_data['memtype'])

            login(request, user)
            return HttpResponseRedirect('/')
        else:
            context={'form': form}
            return render(request, 'registration/register.html',context)
    form = RegistrationForm()
    context={'form': form}
    return render(request, 'registration/register.html',context)

def who(request):
    context = {}
    return render(request, 'who.html', context)

def sharefood(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                                password=form.cleaned_data['password1'],
                                                email=form.cleaned_data['email'],
                                                first_name=str(form.cleaned_data['rname'])+'|'+str(form.cleaned_data['phone']) + '|' + str(
                                                    form.cleaned_data['address']),
                                                last_name=form.cleaned_data['memtype'])

            login(request, user)
            return HttpResponseRedirect('/')
        else:
            context={'form': form}
            return render(request, 'registration/register.html',context)
    form = RegistrationForm()
    context={'form': form}
    return render(request, 'registration/register.html',context)


def latest(request):
    context = {}
    return render(request, 'latest.html', context)

def near(request):
    context = {}
    return render(request, 'near.html', context)

def sale(request):
    context = {}
    return render(request, 'sale.html', context)

def deli(request):
    context = {}
    return render(request, 'deli.html', context)