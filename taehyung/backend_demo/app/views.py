from django.shortcuts import render, get_object_or_404
from .models import Foods,Reply
from django.views.generic import CreateView
from .forms import ReplyForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def post_list(request):
    qs = Foods.objects.all()
    qs_reply = Reply.objects.all()

    context={
        "foods_list" : qs,
        "reply_list" : qs_reply
    }
    return render(request,"app/index.html",context)




class ReplyCreateView(CreateView):
    model = Reply
    form_class = ReplyForm
    template_name = 'app/add_reply.html'

    def form_valid(self, form):
        reply = form.save(commit=False)
        reply.usr = self.request.user
        reply.save()
        return super(ReplyCreateView, self).form_valid(form)


reply_new = login_required(ReplyCreateView.as_view(model=Reply,form_class=ReplyForm,template_name = 'app/add_reply.html'))