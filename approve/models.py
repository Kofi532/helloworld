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
  
class Cals(models.Model):
    username = models.CharField(max_length=15, default='Paste your username here')
    title = models.CharField(max_length=25, default='Type here')
    eventdate = models.DateTimeField(default=timezone.now)
    eventtime = models.CharField(max_length=10, default='HH:MM')
    date  = models.DateTimeField(default=timezone.now)
    approve = models.CharField(max_length=10, default='Pending')



    def __str__(self):
        return self.username
