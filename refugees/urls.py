"""refugees URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
#from reports.views import index
from django.conf.urls import url
from django.contrib import admin
from reports import views
from reports.views import Index, ResourcePage, CityList, StateList

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', Index.as_view()),
    url(r'^background_info/$', views.background_info, name='background_info'),
    url(r'^about/$', views.about, name='about'),
    url(r'^reports/$', StateList.as_view()),
    #url(r'^reports/(?P<state_slug>[\w-]+)/$', views.city_list),
    url(r'^reports/(?P<state_slug>[\w-]+)/$', CityList.as_view()),
    url(r'^reports/(?P<state_slug>[\w-]+)/(?P<city_slug>[\w-]+)/$', views.country_list),
    url(r'^reports/(?P<state_slug>[\w-]+)/(?P<city_slug>[\w-]+)/(?P<country_slug>[\w-]+)/$', views.country_detail),
    url(r'^admin/', admin.site.urls),
    #url(r'^resources/$', views.resources_page, name='resources_page'),
    url(r'^resources/$', ResourcePage.as_view()),
    url(r'^stories/$', views.stories, name='stories'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
