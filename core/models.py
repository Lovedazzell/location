from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserData(models.Model):
    user = models.ForeignKey(User  ,on_delete=models.CASCADE)
    name = models.CharField(max_length=40,null = True, blank= True)
    number = models.BigIntegerField(null=True, blank=True)
    sshot = models.ImageField(upload_to='screenshot/',null=True,blank=True)
    door = models.ImageField(upload_to='doorstep/',null=True,blank=True)
    comment = models.TextField(max_length=1000, null=True,blank=True)
    lat_tude = models.CharField(max_length=40,null=True,blank=True)
    lon_tude = models.CharField(max_length=40,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=300,null=True,blank=True)
