from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def mwanzo(request):
    return render(request,'index.html')



def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form is valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect ('mwanzo')
    else:
        form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})