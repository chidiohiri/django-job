from django.urls import path 
from . import views

urlpatterns = [
    path('add-company/', views.add_company, name='add-company'), 
    path('update-company/<int:pk>/', views.update_company, name='update-company'), 
    path('company-details/<int:pk>/', views.company_details, name='company-details'),
    path('jobs-per-company/<int:pk>/', views.jobs_per_company, name='jobs-per-company')
]