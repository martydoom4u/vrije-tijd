# Django
from django.urls import path
# Local
from todo import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create/', views.todoCreateView.as_view(), name='create_todo'),
    path('update/<int:pk>', views.todoUpdateView.as_view(), name='update_todo'),
    path('read/<int:pk>', views.todoReadView.as_view(), name='read_todo'),
    path('delete/<int:pk>', views.todoDeleteView.as_view(), name='delete_todo')
]