from django.shortcuts import render, get_object_or_404
from .models import Foods,Reply,Corporation
from django.views.generic import CreateView
from .forms import ReplyForm, CorporationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def post_list(request):
    qs = Foods.objects.all()

    qs_reply = Reply.objects.all()
    qs_corporation = Corporation.objects.all()
    

    context={
        "foods_list" : qs,
        "reply_list" : qs_reply,
        "corporation_list":qs_corporation
    }
    return render(request,"app/index.html",context)


def post_list_ordered_star(request):
    
    qs_star = Foods.objects.all().order_by('-star')

    qs_reply = Reply.objects.all()
    qs_corporation = Corporation.objects.all()

    context={   
        
        "star_ordered_list" : qs_star,
        "reply_list" : qs_reply,
        "corporation_list":qs_corporation
    }
    return render(request,"app/ordered_star.html",context)



#Reply Creating and Corporation Creating

class ReplyCreateView(CreateView):
    model = Reply
    form_class = ReplyForm
    template_name = 'app/add_reply.html'

    def form_valid(self, form):
        reply = form.save(commit=False)
        reply.usr = self.request.user
        reply.save()
        return super(ReplyCreateView, self).form_valid(form)

class CorporationCreateView(CreateView):
    model = Corporation
    form_class = CorporationForm
    template_name = 'app/add_corporation.html'

    def form_valid(self, form):
        corporation = form.save(commit=False)
        corporation.usr = self.request.user
        corporation.save()
        return super(CorporationCreateView, self).form_valid(form)


reply_new = login_required(ReplyCreateView.as_view(model=Reply,form_class=ReplyForm,template_name = 'app/add_reply.html'))
corporation_new = login_required(CorporationCreateView.as_view(model=Corporation,form_class=CorporationForm,template_name = 'app/add_corporation.html'))


