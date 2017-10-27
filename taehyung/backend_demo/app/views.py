from django.shortcuts import render
from .models import Foods,Reply

# Create your views here.

def post_list(request):
    qs = Foods.objects.all()
    qs_reply = Reply.objects.all()

    context={
        "foods_list" : qs,
        "reply_list" : qs_reply
    }
    return render(request,"app/index.html",context)