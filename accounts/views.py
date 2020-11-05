from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if passwords match
        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        #check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, 'That username is already taken')
            return redirect('register')

        #Check if email is already taken
        if User.objects.filter(email=email).exists():
            messages.error(request, 'That email is being used')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password, email=email,
        first_name=first_name, last_name=last_name)

        user.save()

        messages.success(request, 'You are now registered and can log in')
        return redirect('login')

    #Dealing with a 'GET' request        
    else:
        return render(request, 'accounts/register.html')



def login(request):
    if request.method == 'POST':
        #get variables
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        #The user was found in the database! He/she exists!
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            #Decide where we will be redirected
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')



        return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')