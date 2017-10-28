from django.conf.urls import url
from . import views

urlpatterns = [
    
    #Lists pages
    url(r'^$', views.post_list, name='post_list'),
    url(r'^ordered_star/$', views.post_list_ordered_star, name='post_list_ordered_star'),    

    #Making New
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^reply/new/$', views.reply_new, name='reply_new'),
    url(r'^corporation/new/$', views.corporation_new, name='corporation_new'),

    #Edit
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

 
]
