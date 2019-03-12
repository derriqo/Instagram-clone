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
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data.get('username')
            new_user.raw_pass = form.clean_data.get('password1')
            new_user.save()
            # authenticate(username=username,password=raw_pass)
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})