from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/',default='profile_pics/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio =models.TextField()
    follows = models.ManyToManyField(User, related_name='follows')

    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()

    @classmethod
    def search_by_username(cls,search_term):
        gram = cls.objects.filter(user__username__icontains=search_term)
        return gram
    
class Image(models.Model):
    author = models.ForeignKey(User,related_name='image',on_delete=models.CASCADE,null=True)
    image_pic = models.ImageField(upload_to="images/",blank=True)
    image_caption = models.CharField(max_length=50, default="")
    date = models.DateTimeField(auto_now=True)


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



    @classmethod
    def get_photos(cls):
       return cls.objects.all()

class Comment(models.Model):
    image = models.ForeignKey(Image, blank=True, on_delete=models.CASCADE, related_name='comment')
    commenter = models.ForeignKey(User, blank=True)
    comment_itself = models.TextField()

    def delete_comment(self):
        self.delete()

    def save_comment(self):
        self.save()

    @classmethod
    def get_comments_on_image(cls, id):
        the_comments = Comment.objects.filter(image__pk=id)
        return the_comments

    def __str__(self):
        return self.comment_itself

  



    