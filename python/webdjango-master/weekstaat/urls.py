from django.urls import path
from weekstaat import views



urlpatterns = [
    path('', views.Index.as_view(), name='indexs'),
    path('create/', views.WeekstaatCreateView.as_view(), name='create_Weekstaat'),
    path('update/<int:pk>', views.WeekstaatUpdateView.as_view(), name='update_Weekstaat'),
    path('read/<int:pk>', views.WeekstaatReadView.as_view(), name='read_Weekstaat'),
    path('delete/<int:pk>', views.WeekstaatDeleteView.as_view(), name='delete_Weekstaat')
]
