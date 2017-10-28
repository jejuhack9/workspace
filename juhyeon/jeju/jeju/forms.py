#-*- coding: utf-8 -*-
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from jeju.models import *


class RegistrationForm(forms.Form):
    acctype = [('in', u'food donor'),
               ('out', u'food recipient')]
    username = forms.CharField(label='사용자 이름(ID)',min_length=4, max_length=30,help_text=("8~30자의 쉽지 않은 영문+숫자 조합입니다"))
    rname = forms.CharField(label='예금주(실명)', min_length=2, max_length=10, help_text=("2~4자의 한글실명입니다."))
    email = forms.EmailField(label='이메일',help_text=('회원정보 수정시 필요한 이메일 주소입니다.'))
    password1 = forms.CharField(label='비밀번호(PW)',widget=forms.PasswordInput(),help_text=("8~30자 입니다."),min_length=8,max_length=30)
    password2 = forms.CharField(label='비밀번호 재입력',widget=forms.PasswordInput())
    memtype = forms.ChoiceField(label='회원종류', choices=acctype, widget=forms.RadioSelect())
    phone = forms.CharField(
        label=u'휴대전화',
        help_text=('01X-YYYY-ZZZZ 형식으로 숫자와 하이픈으로만 기입하세요.'),
    )
    address = forms.CharField(label=u'주소', min_length=1, max_length=200, widget=forms.Textarea,
                              help_text=("주소를 알려주세요"))
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'[가-힣]+', username):
            raise forms.ValidationError('아이디에 잘못된 문자가 들어가 있습니다. 한글 불가 합니다.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('이미 등록된 이름입니다. 다른 이름을 쓰세요')

    def clean_phone(self):
        phraw=self.cleaned_data['phone']
        if not str(phraw).__contains__('-'):
            raise forms.ValidationError('휴대전화번호에 하이픈이 없습니다.-로 구분해주세요.')
        else:
            comp=str(phraw).split('-')
            if len(comp) is not 3:
                raise forms.ValidationError('올바른 휴대전화번호 형식이 아닙니다.')
            else:
                for num in comp:
                    try:
                        int(num)
                    except:
                        raise forms.ValidationError('휴대전화번호에 문자가 있습니다.')


class FoodForm(forms.Form):
    apikey = forms.CharField(label=u'고유key', max_length=32)
    acctype = [('free', u'free food'),
               ('discount sale', u'discount sale')]
    price = forms.IntegerField(label='가격')
    percent=forms.IntegerField(label='할인율')
    sharetype = forms.ChoiceField(label='판매종류', choices=acctype, widget=forms.RadioSelect())
    fname = forms.CharField(label='음식 이름(ID)',min_length=8, max_length=30)
    fcontent = forms.CharField(label='음식(정보)', min_length=2, max_length=2000)
    stime = forms.CharField(label='생성시각', min_length=5, max_length=5, help_text=("13:23"))
    etime = forms.CharField(label='종료시각', min_length=5, max_length=5, help_text=("15:41"))
