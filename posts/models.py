from django.db import models
from django.utils import timezone
import uuid


COLOR_CHOICES = (
    ('yes','Yes'),
    ('no', 'No'),
)



class Post(models.Model):
    title = models.TextField(max_length=20, default='type here')
    content = models.TextField(max_length=60, default='type here')
    image = models.ImageField(default='Please upload image')
    surname = models.CharField(max_length=25, default='type here')
    firstname = models.CharField(max_length=25, default='type here')
    level = models.CharField(max_length=25, default='type here')
    date  = models.DateTimeField(default=timezone.now)
    idd = models.CharField(max_length=50, default=uuid.uuid1())
    approve = models.CharField(max_length=5, default='No')

    def __str__(self):
        return self.title

class Post_a(models.Model):

    Approve = models.CharField(max_length=6, choices=COLOR_CHOICES, default='.')
    Comments = models.CharField(max_length=50, default='.')
    Date =  models.DateTimeField(default=timezone.now)
    idd = models.CharField(max_length=50, default="Clear and paste here")


    def __str__(self):
        return self.Approve

class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='uploads/', default='newbalance.jpg', height_field=None, width_field=None)
    studio_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    description_short = models.TextField()
    description_long = models.TextField()
    keywords = models.CharField(max_length=255)
    date = models.DateTimeField('DateAdded',
             auto_now=True, auto_now_add=False)

    class Meta:
        db_table = "experience"

    def __str__(self):
        return self.studio_name + ' ' + self.duration
# Create your models here.
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='uploads/', default='newbalance.jpg', height_field=None, width_field=None)
    studio_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    description_short = models.TextField()
    description_long = models.TextField()
    keywords = models.CharField(max_length=255)
    date = models.DateTimeField('DateAdded',
             auto_now=True, auto_now_add=False)