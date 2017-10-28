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
from django.urls import reverse

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
            rname=str(form.cleaned_data['rname'])
            phm=str(form.cleaned_data['phone'])
            addr=str(form.cleaned_data['address'])
            meta=rname+'|'+ phm + '|' +addr
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                                password=form.cleaned_data['password1'],
                                                email=form.cleaned_data['email'],
                                                first_name=meta,
                                                last_name=form.cleaned_data['memtype'])

            login(request, user)
            if user.last_name.__contains__('in') :
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
            return HttpResponse('x')
    else:
        if request.user.is_authenticated:
            form = FoodForm()
            apikey = str(uuid.uuid4().hex)
            context = {'form': form, 'genkey': apikey}
            return render(request, 'sharefood.html', context)
        else:
            return HttpResponseRedirect('../login')

def landing(request):
    context = {}
    return render(request, 'landing.html', context)

def latest(request):
    last= Foods.objects.all().order_by('-enddate')

    arr = []
    arr2= []
    for i,item in enumerate(last.values()):
        if i<len(last)/2:
            #context = {'fname': item['fname'], 'rname': item['fcontent'], 'sdate': item['startdate'], 'edate': item['enddate']}
            allcs = CsFile.objects.filter(apikey=item['apikey'])
            picd=None
            for pic in allcs.values():
                if picd is None:
                    picd=pic['file']
                else:
                    break
            arr.append([item['fname'],item['tell'],str(item['startdate'])[:19],str(item['enddate'])[:19],item['where'],picd])
            #company = get_object_or_404(Corporation, pk=item['usr'])
            #usrm=get_object_or_404(User, pk=item['usr'])
            #info={}
            #context={'fname':item['fname'],'rname':item['rname'],'sdate':item['startdate'],'edate':item['enddate'],'tel':item['usr']['first_name']}
            #print(item)
        else:
            #context = {'fname': item['fname'], 'rname': item['fcontent'], 'sdate': item['startdate'], 'edate': item['enddate']}
            allcs = CsFile.objects.filter(apikey=item['apikey'])
            picd=None
            for pic in allcs.values():
                if picd is None:
                    picd=pic['file']
                else:
                    break
            arr2.append([item['fname'],item['tell'],str(item['startdate'])[:19],str(item['enddate'])[:19],item['where'],picd])
            #company = get_object_or_404(Corporation, pk=item['usr'])
            #usrm=get_object_or_404(User, pk=item['usr'])
            #info={}
            #context={'fname':item['fname'],'rname':item['rname'],'sdate':item['startdate'],'edate':item['enddate'],'tel':item['usr']['first_name']}
            #print(item)
    context={'list':arr,'list2':arr2}
    return render(request, 'latest.html', context)

def near(request):
    context = {}
    return render(request, 'near.html', context)

def sale(request):
    last = Foods.objects.all().order_by('-percent')

    arr = []
    arr2 = []
    for i, item in enumerate(last.values()):
        if i < len(last) / 2:
            # context = {'fname': item['fname'], 'rname': item['fcontent'], 'sdate': item['startdate'], 'edate': item['enddate']}
            allcs = CsFile.objects.filter(apikey=item['apikey'])
            picd = None
            for pic in allcs.values():
                if picd is None:
                    picd = pic['file']
                else:
                    break
            arr.append(
                [item['fname'], item['tell'], item['percent'], str(item['enddate'])[:19], item['where'],
                 picd])
            # company = get_object_or_404(Corporation, pk=item['usr'])
            # usrm=get_object_or_404(User, pk=item['usr'])
            # info={}
            # context={'fname':item['fname'],'rname':item['rname'],'sdate':item['startdate'],'edate':item['enddate'],'tel':item['usr']['first_name']}
            # print(item)
        else:
            # context = {'fname': item['fname'], 'rname': item['fcontent'], 'sdate': item['startdate'], 'edate': item['enddate']}
            allcs = CsFile.objects.filter(apikey=item['apikey'])
            picd = None
            for pic in allcs.values():
                if picd is None:
                    picd = pic['file']
                else:
                    break
            arr2.append(
                [item['fname'], item['tell'], item['percent'], str(item['enddate'])[:19], item['where'],
                 picd])
            # company = get_object_or_404(Corporation, pk=item['usr'])
            # usrm=get_object_or_404(User, pk=item['usr'])
            # info={}
            # context={'fname':item['fname'],'rname':item['rname'],'sdate':item['startdate'],'edate':item['enddate'],'tel':item['usr']['first_name']}
            # print(item)
    context = {'list': arr, 'list2': arr2}
    return render(request, 'sale.html', context)

def deli(request):
    qs_reply = Reply.objects.all().order_by('-created_at')
    qs_corporation = Corporation.objects.all()

    context = {

        "reply_list" : qs_reply,
        "corporation_list":qs_corporation
    }
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

# def foodreg(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = FoodForm(request.POST)
#             now=str(datetime.datetime.now(tz)).replace('-', '').replace(' ', '').replace(':', '').replace('.', '')[:-3]
#             st=datetime.datetime.now(tz)
#             et = datetime.datetime.now(tz)
#             # st.replace(hour=int(form.cleaned_data['stime'].split(':')[0]),minute=int(form.cleaned_data['stime'].split(':')[1]))
#             # et.replace(hour=int(form.cleaned_data['etime'].split(':')[0]),
#             #            minute=int(form.cleaned_data['etime'].split(':')[1]))
#             # food = Foods.objects.create(usr=request.user,fname=form.cleaned_data['fname'],fcontent=form.cleaned_data['fcontent'],price=form.cleaned_data['price'],percent=form.cleaned_data['percent'],startdate=st,enddate=et,apikey=form.cleaned_data['apikey'])
#             st.replace(hour=int(request.POST.get("stime").split(':')[0]),minute=int(request.POST.get("stime").split(':')[1]))
#             et.replace(hour=int(request.POST.get("etime").split(':')[0]),
#                        minute=int(request.POST.get("etime").split(':')[1]))
#             food = Foods.objects.create(usr=request.user,fname=request.POST.get("fname"),fcontent=request.POST.get("fcontent"),price=request.POST.get("price"),percent=request.POST.get("percent"),startdate=st,enddate=et,apikey=request.POST.get("apikey"))
#             return reverse('latest')
#     else:
#         return HttpResponseRedirect('../login')

def foodreg(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FoodForm(request.POST)
            if form.is_valid():
                now = str(datetime.datetime.now(tz)).replace('-', '').replace(' ', '').replace(':', '').replace('.','')[:-3]
                st=datetime.datetime.now(tz)
                et = datetime.datetime.now(tz)
                print(form.cleaned_data['stime'])
                print(form.cleaned_data['etime'])
                st.replace(hour=int(form.cleaned_data['stime'].split(':')[0]),minute=int(form.cleaned_data['stime'].split(':')[1]))
                et.replace(hour=int(form.cleaned_data['etime'].split(':')[0]),minute=int(form.cleaned_data['etime'].split(':')[1]))
                print(st)
                print(et)
                food = Foods.objects.create(usr=request.user,fname=form.cleaned_data['fname'],fcontent=form.cleaned_data['fcontent'],price=form.cleaned_data['price'],percent=form.cleaned_data['percent'],startdate=st,enddate=et,apikey=form.cleaned_data['apikey'],where=form.cleaned_data['where'],tell=form.cleaned_data['tell'])
                return apps(request)
            else:
                return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('../login')

def apps(request):
    if request.user.is_authenticated:
        return latest(request)
    else:
        return HttpResponseRedirect('../login')

class ReplyCreateView(CreateView):
    model = Reply
    form_class = ReplyForm
    template_name = 'add_reply.html'

    def form_valid(self, form):
        reply = form.save(commit=False)
        reply.usr = self.request.user
        reply.save()
        return super(ReplyCreateView, self).form_valid(form)


reply_new = login_required(ReplyCreateView.as_view(model=Reply,form_class=ReplyForm,template_name = 'add_reply.html'))