from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/',default='profile_pics/')
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio =models.TextField()
    follows = models.ManyToManyField(User, related_name='follows',blank = True)
    
    def save_profile(self):
        self.save()

    @classmethod
    def search_by_username(cls,search_term):
        gram = cls.objects.filter(username__icontains=search_term)
        return news
    
class Image(models.Model):
    image_pic = models.ImageField(upload_to="images/",blank=True)
    image_name = models.CharField(max_length=30,null=True)
    image_caption = models.CharField(max_length=50, default="")
    profile = models.ForeignKey(Profile, null=True)
    likes = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add = True,null = True)

    def save_image(self):
       """
       This is the function that we will use to save the instance of this class
       """
       self.save()

    def search_by_username(cls, search_term):
        images = cls.objects.filter(image_caption__icontains=search_term)
        return images
   
    def total_likes(self):
       return self.likes.count

 

    def delete_image(self):
       """
       This is the function that we will use to delete the instance of this class
       """
       Image.objects.get(id = self.id).delete()

   
    def get_absolute_url(self): 
        return reverse('home') 

    @classmethod
    def get_photos(cls):
       return cls.objects.all()

   
  



    