from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, null=True)
    website = models.URLField(max_length=255)
    email = models.EmailField(max_length=255)
    is_verified = models.BooleanField(default=False)
    cac = models.FileField(upload_to='company_documents/')

    created_on = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name 
