# models.py file

from django.db import models
from django.contrib.auth.models import AbstractUser


from django.contrib.auth.models import BaseUserManager


#model file
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=30, unique=True,)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    block = models.IntegerField(default=0)
    room = models.IntegerField(default=0)
    bed = models.CharField(max_length=10)
    
 


