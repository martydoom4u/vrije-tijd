from django.urls import path
from factuur import views


urlpatterns = [
    path('', views.index, name='index'),
    path(r'create/', views.toevoegen, name='create_factuur'),
]
