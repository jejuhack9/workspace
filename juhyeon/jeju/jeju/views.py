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
import uuid
import jeju.matzip as matzip
from django.utils import timezone
import pytz
from .forms import ReplyForm, CorporationForm
from django.views.generic import CreateView
from .forms import ReplyForm, CorporationForm
from django.contrib.auth.decorators import login_required

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
            if user.last_name is 'in':
                return HttpResponseRedirect('../comreg')
            else:
                return HttpResponseRedirect('/')
        else:
            context={'form': form}
            return render(request, 'registration/register.html',context)
    form = RegistrationForm()
    context={'form': form}
    return render(request, 'registration/register.html',context)

def comreg(request):
    context = {}
    return render(request, 'comreg.html', context)


def who(request):
    context = {}
    return render(request, 'who.html', context)

def sharefood(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            print("form is valid")
            apikey = request.POST['apikey']
            filearr = []
            for key, value in request.FILES.items():
                if (str(value.name).endswith('.jpg') or str(value.name).endswith('.png') or str(value.name).endswith('.JPG') or str(value.name).endswith('.PNG')):
                    newfile = CsFile.objects.create(apikey=apikey,usr=request.user,file=value,regdate=datetime.datetime.now(tz))
            return HttpResponse('o')
        else:
            print(form.errors)
            # return HttpResponseRedirect(reverse('recl'))
            # return HttpResponseRedirect("www.daum.net")
            return HttpResponse('x')
    else:
        if request.user.is_authenticated:
            form = FoodForm()
            apikey = str(uuid.uuid4().hex)
            context = {'form': form, 'genkey': apikey}
            return render(request, 'sharefood.html', context)
        else:
            return HttpResponseRedirect('../login')


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

def jsonapi(request,keyword):
    rst=matzip.search(keyword)
    js = json.dumps(rst, ensure_ascii=False)
    return HttpResponse(js, content_type=u"application/json; charset=utf-8", status=200)

class CorporationCreateView(CreateView):
    model = Corporation
    form_class = CorporationForm
    template_name = 'add_corporation.html'

    def form_valid(self, form):
        corporation = form.save(commit=False)
        corporation.usr = self.request.user
        corporation.save()
        return super(CorporationCreateView, self).form_valid(form)

corporation_new = login_required(CorporationCreateView.as_view(model=Corporation,form_class=CorporationForm,template_name = 'add_corporation.html'))

def foodreg(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FoodForm(request.POST)
            if form.is_valid():
                now=str(datetime.datetime.now(tz)).replace('-', '').replace(' ', '').replace(':', '').replace('.', '')[:-3]

                st=datetime.datetime.now(tz)
                et = datetime.datetime.now(tz)
                st.replace(hour=int(form.cleaned_data['stime'].split(':')[0]),minute=int(form.cleaned_data['stime'].split(':')[1]))
                et.replace(hour=int(form.cleaned_data['etime'].split(':')[0]),
                           minute=int(form.cleaned_data['etime'].split(':')[1]))
                food = Foods.objects.create(usr=request.user,fname=form.cleaned_data['fname'],fcontent=form.cleaned_data['fcontent'],price=form.cleaned_data['price'],percent=form.cleaned_data['percent'],\
startdate=st,enddate=et,apikey=form.cleaned_data['apikey'])
                return HttpResponseRedirect('../../latest')

            else:
                return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('../login')