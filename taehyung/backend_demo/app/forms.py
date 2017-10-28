from django import forms
from .models import Reply, Corporation


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
