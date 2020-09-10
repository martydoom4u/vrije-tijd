# Django
from django.urls import path
# Local
from factuuren import views

urlpatterns = [
    path('', views.Index.as_view(), name='indexf'),
    path('create/', views.FactuurenCreateView.as_view(), name='create_Factuurtje'),
    path('update/<int:pk>', views.FactuurenUpdateView.as_view(), name='update_Factuur'),
    path('read/<int:pk>', views.FactuurenReadView.as_view(), name='read_Factuur'),
    path('delete/<int:pk>', views.FactuurenDeleteView.as_view(), name='delete_Factuur')
]