from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username