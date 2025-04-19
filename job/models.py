from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from company.models import Company
from resume.models import Resume

User = get_user_model()

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=400)
    state = models.CharField(
        max_length=20, 
        choices=(
            ('Lagos', 'Lagos'), 
            ('Abuja', 'Abuja'), 
            ('Kano', 'Kano'), 
            ('Rivers', 'Rivers')
        )
    )
    city = models.CharField(max_length=100)
    min_experience_years = models.PositiveIntegerField()
    job_field = models.CharField(
        max_length=100, 
        choices=(
            ('Marketing', 'Marketing'), 
            ('Information Technology', 'Information Technology'), 
            ('Finance', 'Finance'), 
            ('Accounting', 'Accounting'), 
            ('Design', 'Design'), 
            ('Healthcare', 'Healthcare'), 
            ('Engineering', 'Engineering')
        )
    )
    salary = models.PositiveIntegerField()
    responsibility = models.TextField()
    qualification = models.TextField()
    perks = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField()
    is_verified = models.BooleanField(default=False)
    is_disabled = models.CharField(
        max_length=20, 
        choices=(
            ('True', 'True'), 
            ('False', 'False')
        ), 
        default='False'
    )

    def __str__(self):
        return self.title
    
    def has_expired(self):
        return date.today() > self.expiry_date
    
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    applied_on = models.DateTimeField(auto_now_add=True)
    
class SavedJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    saved_on = models.DateTimeField(auto_now_add=True)