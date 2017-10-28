from django.conf.urls import url
from . import views

urlpatterns = [
    
    #Lists
    url(r'^$', views.post_list, name='post_list'),
    url(r'^ordered_star/$', views.post_list_ordered_star, name='post_list_ordered_star'),    
    
    url(r'^reply/new/$', views.reply_new, name='reply_new'),
    url(r'^corporation/new/$', views.corporation_new, name='corporation_new'),

 
]
