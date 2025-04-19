from django.urls import path
from . import views 

urlpatterns = [
    path('create-job/', views.create_job, name='create-job'), 
    path('update-job/<int:pk>/', views.update_job, name='update-job'), 
    path('delete-job/<int:pk>/', views.delete_job, name='delete-job'), 
    path('my-jobs/', views.my_jobs, name='my-jobs'), 
    path('applications-per-job/<int:pk>/', views.applications_per_job, name='applications-per-job'), 
    path('apply-to-job/<int:pk>/', views.apply_to_job, name='apply-to-job'), 
    path('job-details/<int:pk>/', views.job_details, name='job-details'), 
    path('save-job/<int:pk>/', views.save_job, name='save-job'), 
    path('my-saved-jobs/', views.my_saved_jobs, name='my-saved-jobs' ), 
    path('delete-job-application/<int:pk>/', views.delete_job_application, name='delete-job-application'), 
    path('delete-saved-job/<int:pk>/', views.delete_saved_job, name='delete-saved-job')
]