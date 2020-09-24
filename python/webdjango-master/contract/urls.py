# Django
from django.urls import path
# Local
from contract import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create/', views.ContractCreateView.as_view(), name='create_Contract'),
    path('update/<int:pk>', views.ContractUpdateView.as_view(), name='update_Contract'),
    path('read/<int:pk>', views.ContractReadView.as_view(), name='read_Contract'),
    path('delete/<int:pk>', views.ContractDeleteView.as_view(), name='delete_Contract')
]