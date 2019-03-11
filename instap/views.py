from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def mwanzo(request):
    return render(request,'index.html')



def registration(request):
    form = UserCreationForm
    return render(request,'insta/register.html',{'form':form})