from django.db import models
import datetime
from django.contrib.auth.models import User
from django.conf import settings


class Searchedkey(models.Model):
    usr=models.ForeignKey(settings.AUTH_USER_MODEL ,blank = True, null = True)
    ipaddr=models.CharField(u'IP주소', max_length=200)
    content = models.CharField(u'검색내용', max_length=200)
    update = models.DateTimeField(u'사용일시', auto_now=True)  # 최종업데이트 날짜
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
    regdate = models.DateTimeField(u'생성일시', auto_now=True)
    startdate = models.DateTimeField(u'시작일시', auto_now_add=True)
    enddate = models.DateTimeField(u'종료일시', auto_now_add=True)
    def __str__(self):
        return str(self.time)+" "+str(self.usr)+" "+self.fname+" "+self.fcontent

class Reply(models.Model):
    usr = models.ForeignKey(settings.AUTH_USER_MODEL ,blank = True, null = True)
    message = models.TextField()
    created_at = models.DateTimeField(u'생성일시', auto_now=True)
    star = models.IntegerField(u'평점', default=0)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('app:post_list')#, kwargs={'pk': self.pk})

    
    def __str__(self):
        return self.message

    def __unicode__(self):
        return 

