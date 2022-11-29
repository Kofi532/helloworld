import email
from email import message
from django.db import models
from django.db import models
from django.utils import timezone
from django.db import models


class Post(models.Model):
    surname = models.CharField(max_length=25, default='..')
    firstname = models.CharField(max_length=25, default='..')
    email = models.EmailField(default='..')
    message = models.TextField(max_length=50, default='..')

    def __str__(self):
        return self.surname


class Clubm(models.Model):
    username = models.CharField(max_length=10, default='Paste here')
    surname = models.CharField(max_length=20, default='Type here')
    firstname = models.CharField(max_length=25, default='Type here')
    level = models.TextField(max_length=10, default='Type here')
    title = models.CharField(max_length=25, default='Type here')
    message = models.TextField(max_length=50, default='Type here')
    image = models.ImageField(default='Please upload image')
    date  = models.DateTimeField(default=timezone.now)
    approve = models.CharField(max_length=10, default='Pending')
    
    def __str__(self):
        return self.surname

class Sportm(models.Model):
    username = models.CharField(max_length=10, default='Paste here')
    surname = models.CharField(max_length=10, default='Type here')
    firstname = models.CharField(max_length=25, default='Type here')
    level = models.TextField(max_length=10, default='Type here')
    title = models.CharField(max_length=25, default='Type here')
    message = models.TextField(max_length=50, default='Type here')
    image = models.ImageField(default='Please upload image')
    date  = models.DateTimeField(default=timezone.now)
    approve = models.CharField(max_length=10, default='Pending')

    def __str__(self):
        return self.surname

dayc = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Firday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday')
)
monthc = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April','April'),
    ('May','May'),
    ('June','June'),
    ('July','July'),
    ('August','August'),
    ('September','September'),
    ('October','October'),
    ('November','November'),
    ('December','December'),
)
yearc = (
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
)
timec = (
    ('AM', 'AM'),
    ('PM', 'PM'),
 )
