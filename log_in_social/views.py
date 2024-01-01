from django.shortcuts import render
# from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def social_login(request):
    return render(request,'social_login.html')

def profile(request):
    return render(request, 'profile.html')
