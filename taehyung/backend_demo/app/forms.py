from django import forms
from .models import Reply, Corporation



class ReplyForm(forms.ModelForm):

     class Meta:
        model = Reply
        fields = ['message']
        labels ={
        'message':('내용'),
        }


class CorporationForm(forms.ModelForm):
    
     class Meta:
        model = Corporation
        fields = ['corp_logo']
        labels ={
        'corp_logo':('회사 로고'),
        }