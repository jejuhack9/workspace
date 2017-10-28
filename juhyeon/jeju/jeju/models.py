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
from sorl.thumbnail import ImageField


class Searchedkey(models.Model):
    usr=models.ForeignKey(settings.AUTH_USER_MODEL ,blank = True, null = True)
    ipaddr=models.CharField(u'IP주소', max_length=200)
    content = models.CharField(u'검색내용', max_length=200)
    update = models.DateTimeField(u'사용일시', default=datetime.date.today)  # 최종업데이트 날짜
    def __str__(self):
        return str(self.usr)

class Foods(models.Model):
    @property
    def user(self):
        return User.objects.get(pk=self.user_id)
    time = models.IntegerField(default=0, verbose_name='발송 시각', )
    usr=models.ForeignKey(settings.AUTH_USER_MODEL ,blank = True, null = True)
    fname = models.CharField(u'음식이름', max_length=30, default='null')
    fcontent=models.CharField(u'음식정보', max_length=1000)
    star = models.IntegerField(u'평점', default=0)
    price = models.IntegerField(u'가격', default=0,null = True)
    percent = models.IntegerField(u'할인율', default=0,null = True)
    where = models.CharField(u'음식점위치', max_length=50)
    apikey = models.CharField(u'고유키', max_length=200, default='null')
    gps= models.CharField(u'gps좌표', max_length=30, default='null')
    isdone=models.BooleanField(u'낙찰여부',default=False)
    # issell=models.BooleanField(u'응답생성여부',default=False)
    regdate = models.DateTimeField(u'생성일시', default=datetime.date.today)
    startdate = models.DateTimeField(u'시작일시', default=datetime.date.today)
    enddate = models.DateTimeField(u'종료일시', default=datetime.date.today)
    def __str__(self):
        return str(self.time)+" "+str(self.usr)+" "+self.fname

class CsFile(models.Model):
    usr=models.ForeignKey(settings.AUTH_USER_MODEL ,blank = True, null = True)
    apikey = models.CharField(u'APIkey', max_length=32, default='null')
    file = models.FileField(upload_to='files/%Y%m%d/')
    #file = models.CharField(u'파일이름', max_length=100,default='null')
    regdate = models.DateTimeField(u'등록일시', default=datetime.date.today)  # 최종업데이트 날짜
    update = models.DateTimeField(u'갱신일시', default=datetime.date.today)  # 최종업데이트 날짜
    logcnt=models.IntegerField(u'등록로그수',default=0)
    def __str__(self):
        return str(self.file)


class Reply(models.Model):
    usr = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(u'생성일시', auto_now=True)
    star = models.IntegerField(u'평점', default=0)
    before_picture = ImageField(upload_to='photos', null=True, blank=True)
    after_picture = ImageField(upload_to='photos', null=True, blank=True)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('deli')  # , kwargs={'pk': self.pk})

    def __str__(self):
        return self.message


class Corporation(models.Model):
    usr = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    corp_logo = models.FileField(upload_to='files/%Y%m%d/')
    corp_descriptioin = models.TextField()
    corp_location = models.TextField(max_length=200)
    corp_coordinates = models.CharField(max_length=50)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('sharefood')  # , kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.usr)





