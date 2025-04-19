from django.urls import path 
from . import views 

urlpatterns = [
    path('add-resume/', views.add_resume, name='add-resume'), 
    path('update-resume/<int:pk>/', views.update_resume, name='update-resume'), 
    path('resume-details/<int:pk>/', views.resume_details, name='resume-details'), 
    path('applications-per-resume', views.applications_per_resume, name='applications-per-resume')
]