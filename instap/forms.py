from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Image


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CreatePost(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_pic','image_caption']
        

        