from django.shortcuts import render


def mwanzo(request):
    return render(request,'index.html')