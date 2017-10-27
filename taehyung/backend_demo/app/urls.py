from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^reply/new/$', views.reply_new, name='reply_new'),
]