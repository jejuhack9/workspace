#-*- coding: utf-8 -*-
# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
#from django.utils import timezone


class Searchedkey(models.Model):
    usr=models.ForeignKey(settings.AUTH_USER_MODEL ,blank = True, null = True)
    ipaddr=models.CharField(u'IP주소', max_length=200)
    content = models.CharField(u'검색내용', max_length=200)
    update = models.DateTimeField(u'사용일시', default=datetime.date.today)  # 최종업데이트 날짜
    def __str__(self):
        return str(self.usr)

class Foods(models.Model):
    time = models.IntegerField(default=0, verbose_name='발송 시각', )
    usr=models.ForeignKey(settings.AUTH_USER_MODEL ,blank = True, null = True)
    fname = models.CharField(u'음식이름', max_length=30, default='null')
    fcontent=models.CharField(u'음식정보', max_length=2000)
    star = models.IntegerField(u'평점', default=0)
    price = models.IntegerField(u'가격', default=0)
    where = models.CharField(u'음식점위치', max_length=50)
    rinfo = models.CharField(u'음식점기본정보', max_length=200, default='null')
    gps= models.CharField(u'gps좌표', max_length=30, default='null')
    isdone=models.BooleanField(u'낙찰여부',default=False)
    file1 = models.FileField(upload_to='files/%Y%m%d/')
    file2 = models.FileField(upload_to='files/%Y%m%d/')
    file3 = models.FileField(upload_to='files/%Y%m%d/')
    file4 = models.FileField(upload_to='files/%Y%m%d/')
    file5 = models.FileField(upload_to='files/%Y%m%d/')
    issell=models.BooleanField(u'응답생성여부',default=False)
    regdate = models.DateTimeField(u'생성일시', default=datetime.date.today)
    startdate = models.DateTimeField(u'시작일시', default=datetime.date.today)
    enddate = models.DateTimeField(u'종료일시', default=datetime.date.today)
    def __str__(self):
        return str(self.time)+" "+str(self.usr)+" "+self.fname+" "+self.fcontent


class Reply(models.Model):
    #형 위에거 참고하셔서 만들어주세요