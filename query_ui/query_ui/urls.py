"""query_ui URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from indexing import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
    url(r'^index/', views.index, name = 'index'),
    url(r'^search/', views.search, name = 'search'),
    url(r'^classifyResults/', views.classifyResults, name = 'classifyResults'),
    url(r'^classify/', views.classify, name = 'classify'),
    url(r'^template/', views.template, name = 'template'),
    url(r'^job_details/(?P<pk>\d*)/$', views.job_details, name='job_details'),
    # url(r'^job_details/(?P<pk>\s*)/$', views.job_details, name='job_details')
]
