import email
from email import message
from django.db import models
from django.db import models
from django.utils import timezone

class Post(models.Model):
    surname = models.CharField(max_length=25, default='..')
    firstname = models.CharField(max_length=25, default='..')
    email = models.EmailField(default='..')
    message = models.TextField(max_length=50, default='..')

    def __str__(self):
        return self.surname