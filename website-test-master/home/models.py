from django.db import models
from django.contrib import auth
# Create your models here. 


class Event(models.Model):
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=3)

    def __str__(self):
    	return self.name