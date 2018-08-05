"""grad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from jobboard import views as job_views
from login import views

urlpatterns = [

    path('admin/', admin.site.urls),
    #re_path(r'^login/$', auth_views.login(template_name = 'accounts/login.html'), name='login'),
    re_path(r'^signup/$', views.signup, name='signup'),
    path('login/', include('login.urls')),
	path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('jobs/', job_views.jobs, name='jobs')
]








