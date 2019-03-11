from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# class Profile(models.Model):
#     profile_pic = models.ImageField()
#     username = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     phone_number = models.CharField(max_length = 10,blank = True)
    
class Image(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)    