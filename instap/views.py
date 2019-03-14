from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,CreatePost
from django.contrib.auth import login,authenticate
from .models import Image


@login_required(login_url='')
def index(request):
    images = Image.objects.all()
    return render(request,'index.html', {'images': images})

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'registration/registration_form.html',{'form':form})  

def search_users(request):

    if 'searchItem' in request.GET and request.GET["searchItem"]:
        search_term = request.GET.get("searchItem")
        searched_users = Profile.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, '',{"message":message,"profile": searched_users})

    else:
        message = "Cant find User"
        return render(request, 'other-temp/search.html',{"message":message})

@login_required(login_url='accounts/')
def profile(request):
    current_user = request.user
    images = Image.objects.filter(author__pk=current_user.id)
    return render(request,'profile.html',{'current_user':current_user,'images':images})

def signout(request):
    logout(request)
    return redirect('login')

def createPost(request):
    current_user = request.user

    form = CreatePost(request.POST,request.FILES)
    if request.method=='POST':
        form = CreatePost(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = CreatePost()
    return render(request,'post.html',{'form':form})

