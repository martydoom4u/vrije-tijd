from django.conf.urls import url
from profiel import views


urlpatterns = [
    url(r'^$', views.profiel,name='profiel'),
]