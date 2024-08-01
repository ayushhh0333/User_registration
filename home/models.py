
from django.db import models
import datetime
from django.utils import timezone


class Customer (models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    contact = models.CharField(max_length=14)
    email = models.EmailField(max_length=254)
    password = models.TextField(max_length=250)
    city = models.TextField(default = 0)
    state = models.TextField(default = 0)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def method(post):
        return f"{post.last_name} {post.last_name}"

    
    

    