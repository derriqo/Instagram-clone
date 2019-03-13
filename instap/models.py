from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    image = models.ImageField(upload_to="images/")
    image_name = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
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
    