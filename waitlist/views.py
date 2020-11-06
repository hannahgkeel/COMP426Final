from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# If the user is not logged in, send to login screen.
@login_required(login_url='/accounts/login')
def index(request):
    return render(request, 'waitlist/waitlist.html')
