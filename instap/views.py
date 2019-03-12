from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login,authenticate

def mwanzo(request):
    return render(request,'index.html')



def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form is valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_pass = form.clean_data.get('password1')
            # authenticate(username=username,password=raw_pass)
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})