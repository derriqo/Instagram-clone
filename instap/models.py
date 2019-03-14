from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime as dt


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/',default='profile_pics/')
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_bio = models.TextField(max_length=30)
    
    def save_profile(self):
        self.save()

    @classmethod
    def search_by_username(cls,search_term):
        gram = cls.objects.filter(username__icontains=search_term)
        return news
    
    
class Image(models.Model):
    username = models.ForeignKey(User, null=True)
    image_pic = models.ImageField(upload_to="images/")
    image_name = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    time_updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, null=True)
    likes = models.PositiveIntegerField(default=0)

    def save_image(self):
        '''
        method to save image
        '''
        self.save()

    def delete_image(self):
        '''
        method to delete image
        '''
        self.delete()
    
    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

class Comment(models.Model):
    username = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user')
    comment = models.CharField(max_length=80, null=True)
    date_posted = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Image, related_name='comments', null=True)

    def __str__(self):
        return self.comment
    
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments

    