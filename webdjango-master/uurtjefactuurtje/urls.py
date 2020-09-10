"""uurtjefactuurtje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls import include
from home import views




urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^home/', include('home.urls')),
    url(r'^weekstaat/', include('weekstaat.urls')),
    url('admin/', admin.site.urls),
    url(r'accounts/', include('accounts.urls', namespace='accounts')),
    url(r'accounts/', include('django.contrib.auth.urls' )),
    url(r'^test/$',views.TestPage.as_view(),name='test'),
    url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    url(r'contract/', include('contract.urls')),
    url(r'profiel/', include('profiel.urls')),
    url(r'factuuren/', include('factuuren.urls')),



]