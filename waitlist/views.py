from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import WaitlistTicket

# If the user is not logged in, send to login screen.
@login_required(login_url='/accounts/login')
def index(request):

    if request.method == 'POST':
        #get variables
        username = request.user
        full_name = request.user.get_full_name()
        location = request.POST['location']
        party_size = request.POST['party_size']

        #If user is already in waitlist, give error
        if WaitlistTicket.objects.filter(user_id=username).exists():
            messages.error(request,'You are already on the waitlist')
            return redirect('waitlist')

        #Else carry on
        else:
            ticket = WaitlistTicket(location=location, party_size=party_size, customer=full_name, user_id=username)
            ticket.save()
            messages.success(request, 'You have been added to the waitlist')
            return redirect('inlist')

    #method is GET
    else:
        return render(request, 'waitlist/waitlist.html')


@login_required(login_url='/accounts/login')
def inlist(request):
    return render(request, 'waitlist/inlist.html')


@login_required(login_url='/accounts/login')
def ready(request):
    return render(request, 'waitlist/ready.html')
