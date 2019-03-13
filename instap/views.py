from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login,authenticate


@login_required(login_url='accounts/')
def mwanzo(request):
    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('/accounts/login/')
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
        return render(request, '',{"message":message})

@login_required(login_url='accounts/')
def profile(request,username)
