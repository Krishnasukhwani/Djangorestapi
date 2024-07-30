from django.db import models

# Create your models here.

#Creating Company Model
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),
                                                  ('NON IT' , 'NON IT'),
                                                  ('Android dev','Android dev')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
#Creating Employee Model

class Employee(models.Model):
    name=models.CharField(max_length=100)
    emailid=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    designation=models.CharField(max_length=100,choices=(('Manager','manager'),
                                                  ('Team Lead' , 'tl'),
                                                  ('Software developer','sd')))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)