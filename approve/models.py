from django.db import models
from django import forms
from django.utils import timezone  

COLOR_CHOICES = (
    ('yes','Yes'),
    ('no', 'No'),
)

class Post(models.Model):

    Approve = models.CharField(max_length=6, choices=COLOR_CHOICES, default='None')
    Comments = models.CharField(max_length=50,  default='None')
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.Approve
  
 
