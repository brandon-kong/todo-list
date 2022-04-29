import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

PRIORITIES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
)

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True, max_length=200)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

class Item(models.Model):
    text = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    urgency = models.CharField(choices=PRIORITIES, default='none', max_length=20)
    time_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text #+ " added by " + self.author.username