from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),
    path('upload/', views.upload_report, name='upload_report'),
    path('<int:pk>/', views.report_detail, name='report_detail'),
    path('reminders/add/', views.add_reminder, name='add_reminder'),
    path('emergency/', views.emergency_info, name='emergency_info'),
]
