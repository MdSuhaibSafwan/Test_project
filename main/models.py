from django.db import models
from django.contrib.auth.models import User


class Content(models.Model):
    # user --> content (one to many)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    title = models.CharField(max_length=150)
    text = models.TextField()    

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # models.OneToOneRel
    phone = models.CharField(max_length=15)    
    address_1 = models.TextField()
    address_2 = models.TextField()

    def __str__(self):
        return self.user.username
