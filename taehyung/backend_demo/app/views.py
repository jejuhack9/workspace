from django.shortcuts import render, get_object_or_404
from .models import Foods,Reply,Corporation
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import ReplyForm, CorporationForm, FoodModelForm
from django.contrib.auth.decorators import login_required


def post_list(request):
    qs = Foods.objects.all().order_by('-regdate')

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


def post_list_ordered_discount(request):
    
    qs_discount = Foods.objects.all().order_by('-percent')


    qs_reply = Reply.objects.all()
    qs_corporation = Corporation.objects.all()

    context={   
        
        "discount_ordered_list" : qs_discount,
        "reply_list" : qs_reply,
        "corporation_list":qs_corporation
    }
    return render(request,"app/ordered_discount.html",context)

#Foods Creating and Reply Creating and Corporation Creating
class FoodsCreateView(CreateView):
    model = Foods
    form_class = FoodModelForm
    template_name = 'app/add_food.html'

    def form_valid(self, form):
        posts = form.save(commit=False)
        posts.usr = self.request.user
        posts.save()
        return super(FoodsCreateView, self).form_valid(form)


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


#Making New
post_new = login_required(FoodsCreateView.as_view(model=Foods,form_class=FoodModelForm, template_name = 'app/add_food.html'))
reply_new = login_required(ReplyCreateView.as_view(model=Reply,form_class=ReplyForm,template_name = 'app/add_reply.html'))
corporation_new = login_required(CorporationCreateView.as_view(model=Corporation,form_class=CorporationForm,template_name = 'app/add_corporation.html'))

#Edit
post_edit = login_required(UpdateView.as_view(model=Foods, form_class=FoodModelForm, template_name = 'app/add_food.html'))


