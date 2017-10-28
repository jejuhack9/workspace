"""deff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib.auth import views as autho
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from jeju.views import *
import mysite.settings


urlpatterns = [
    url(r'^$', landing),
    url(r'^search/', search),
    url(r'^admin/', admin.site.urls),
    url(r'^login/',autho.login,{'template_name':'login.html'},name='login'),
    url(r'^logout/',autho.logout,{'template_name':'latest.html'},name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^who/', who,name='who'),
    url(r'^latest/', latest,name='latest'),
    url(r'^near/', near,name='near'),
    url(r'^sale/', sale,name='sale'),
    url(r'^deli/', deli,name='deli'),
    url(r'^sharefood/foodreg', foodreg,name='foodreg'),
    url(r'^sharefood/', sharefood,name='sharefood'),
    url(r'^jsonapi/(?P<keyword>.*)/$', jsonapi, name='jsonapi'),
    url(r'^comreg', corporation_new, name='comreg'),
    url(r'^reply_new',reply_new,name='reply_new'),

]
urlpatterns += static(mysite.settings.MEDIA_URL, document_root=mysite.settings.MEDIA_ROOT)
urlpatterns += static(mysite.settings.STATIC_URL, document_root=mysite.settings.STATIC_ROOT)


