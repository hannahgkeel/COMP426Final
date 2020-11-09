from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import WaitlistTicket

# If the user is not logged in, send to login screen.
@login_required(login_url='/accounts/login')
def index(request):
    username = request.user

    if request.method == 'POST':
        #get variables
        full_name = request.user.get_full_name()
        location = request.POST['location']
        party_size = request.POST['party_size']

        #If user is already in waitlist and has not been served, redirect to inlist
        if WaitlistTicket.objects.filter(user_id=username, customer_is_served=False).exists():
            messages.error(request,'You are already on the waitlist')
            return redirect('inlist')

        #Else carry on
        else:
            ticket = WaitlistTicket(location=location, party_size=party_size, customer=full_name, user_id=username)
            ticket.save()
            messages.success(request, 'You have been added to the waitlist')
            return redirect('inlist')

    #method is GET
    else:

        #Redirect to inlist if the user was already on list but not served..
        if WaitlistTicket.objects.filter(user_id=username, customer_is_served=False).exists():
            return redirect('inlist')


        return render(request, 'waitlist/waitlist.html')



@login_required(login_url='/accounts/login')
def inlist(request):

    #get username
    username = request.user

    #Make sure the user is already in the queue.
    if WaitlistTicket.objects.filter(user_id=username, customer_is_served=False).exists():

        #find user location and check in time in wait list table
        user_location = WaitlistTicket.objects.get(user_id=username, customer_is_served=False).location
        user_check_in_time = WaitlistTicket.objects.get(user_id=username, customer_is_served=False).check_in_time

        #Count number of people ahead of user (including user)
        user_position = WaitlistTicket.objects.filter(location = user_location, check_in_time__lte=user_check_in_time, customer_is_served=False).count()

        context = {
            'user_position': user_position
        }

        #Send this info on render method so we can use it on html
        return render(request, 'waitlist/inlist.html', context)
    else:
        messages.error(request,'Please join the waitlist first.')
        return redirect('waitlist')
