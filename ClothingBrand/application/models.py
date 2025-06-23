from django.db import models

# Create your models here.

class User(models.Model):
    empid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    #def __str__(self):
        #return f"{self.first_name} ({self.username})"
        
class Employee(models.Model):
    empid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}"