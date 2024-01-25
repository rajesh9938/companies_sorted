from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150,unique=True)
    password = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    
class CompaniesSorted(models.Model):
    number = models.CharField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    domain = models.CharField(max_length=200,null=True,blank=True)
    year_founded = models.CharField(max_length=200,null=True,blank=True)
    industry = models.CharField(max_length=200,null=True,blank=True)
    size_range = models.CharField(max_length=200,null=True,blank=True)
    locality = models.CharField(max_length=200,null=True,blank=True)
    country = models.CharField(max_length=200,null=True,blank=True)
    linkedin_url = models.CharField(max_length=200,null=True,blank=True)
    current_employee_estimate = models.CharField(max_length=200,null=True,blank=True)
    total_employee_estimate = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name
    
class CandidateUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150,unique=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name