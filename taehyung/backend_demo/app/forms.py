from django import forms
from .models import Reply, Corporation,Foods


class ReplyForm(forms.ModelForm):
    CHOICES=[
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
         
         ]
    star = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
        
    class Meta:
        model = Reply
        fields = ['message','before_picture','after_picture','star']
        labels={
                'star' : ('평점'),
        }
        widgets = {
        
        'message': forms.Textarea(attrs={
                'style':'height:200px',
                'row' : '3',
                'class': 'form-control', 
                'id' : 'textArea',

                }),
        'before_picture' : forms.ClearableFileInput(attrs={
                'class': 'btn btn-default btn-lg',

                }),

        'after_picture' : forms.ClearableFileInput(attrs={
                'class': 'btn btn-default btn-lg', 

                }),
        }

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


class FoodModelForm(forms.ModelForm):
    class Meta:
        model = Foods
        fields = '__all__'

class CorporationForm(forms.ModelForm):
    
    CHOICES=[('select1','select 1'),
         ('select2','select 2')]

    class Meta:
        model = Corporation
        fields = ['corp_logo','corp_descriptioin','corp_location','corp_coordinates']
        widgets = {

        'corp_logo' : forms.ClearableFileInput(attrs={
                'class': 'btn btn-default btn-lg',

                    }),              
        
        'corp_descriptioin': forms.Textarea(attrs={
                'style':'height:200px',
                'row' : '3',
                'class': 'form-control', 
                'id' : 'textArea',

                    }),
        'corp_location' : forms.TextInput(attrs={
                'style':'height:50px',
                'row' : '3',
                'class': 'form-control', 
                'id' : 'textArea',

                    }),

        'corp_coordinates' : forms.TextInput(attrs={
                'style':'height:50px',
                'row' : '3',
                'class': 'form-control', 
                'id' : 'textArea',

                    }),

        }
