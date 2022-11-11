from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    surname = models.CharField(max_length=25, default='DEFAULT VALUE')
    firstname = models.CharField(max_length=25, default='DEFAULT VALUE')
    level = models.CharField(max_length=25, default='DEFAULT VALUE')
    date = date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

COLOR_CHOICES = (
    ('yes','Yes'),
    ('no', 'No'),
)

class Post_a(models.Model):

    Approve = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
    def __str__(self):
        return self.title

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