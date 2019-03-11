from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def mwanzo(request):
    form = UserCreationForm
    return render(request,'insta/register.html'{'form':form})