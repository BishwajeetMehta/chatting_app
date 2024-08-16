from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    phone= models.CharField(max_length=15,blank=True, null=True, unique=True)
    DoB = models.DateField (blank=True, null=True)
    bio = models.TextField(blank=True,null=True)
    gender = models.CharField(blank=True, null=True,max_length=8)
    permanent_location = models.CharField(max_length=40,blank=True,null=True)
    temporary_location = models.CharField(max_length=40,blank=True,null=True)
    profile =models.ImageField(blank=True, null=True,upload_to='profile_pictures/')
    cover_pic = models.ImageField(blank=True,null=True,upload_to='cover_pictures/')
    status = models.BooleanField(default=1)