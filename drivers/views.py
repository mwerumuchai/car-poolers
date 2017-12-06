from __future__ import absolute_import
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction
from django.http import Http404
from .forms import UserForm,ProfileForm,RequestRideForm
from .models import DriverProfile,Request,CarSharing
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

# Create your views here.
@login_required(login_url='/accounts/register/')
def d_index(request):
    return render(request, 'drivers/d-index.html')

def about(request):
    return render(request, 'about.html')

# profile
@login_required
@transaction.atomic
def update_profile(request,username):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('profiles')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def profile(request,username):
    try:
        user = User.objects.get(username=username)
        profile_pic = DriverProfile.objects.filter(user_id=user).all().order_by('-id')
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'profiles/profile.html', {"user":user, "profile_pic":profile_pic})

# DRIVER
@login_required
def carshare(request,user_id):
    user = User.objects.get(pk=user_id)
    form = CarSharing(request.POST)
    #
    # if user.user.type == 'Rider':
    #     raise Http404
    carsharing = CarDetails.objects.get(pk=cardetails_id, user=user)

    if request.method == 'POST':
        if form.is_valid():
            share = form.save(commit=False)
            share.user = user

            share.start_time = request.POST['start_time']
            share.cardetails = carsharing
            share.save()

            rides = CarDetails.objects.filter(user=user).order_by('pk').reverse()
            shared = CarSharing.objects.filter(user=user).order_by('date').reverse()
            share = CarSharing.objects.filter(user=user).latest('pk')

            return render(request,'vehicle/view_share.html')

        else:
            return render(request,'vehicle/share_ride.html', {"user":user, "carsharing":carsharing, "form":form})

    else:
        return render(request,'vehicle/share_ride.html', {"user":user, "carsharing":carsharing, "form":form})

@login_required
def see_car_shared(request,user_id):
    user = User.objects.get(pk=user_id)

    # if user.user.type == 'Rider':
    #     raise Http404
    rides = CarDetails.objects.filter(user=user).order_by('pk').reverse()
    shared = CarSharing.objects.filter(user=user).order_by('date').reverse()
    request = Request.objects.filter(carsharing=shared)

    return render(request, 'vehicle/view_share.html')

@login_required
def request_ride(request,user_id,carsharing_id):
    user = User.objects.get(pk=user_id)
    carsharing = CarSharing.objects.get(pk=carsharing_id)
    form = RequestRideForm(reuqest.POST)

    if request.method == 'POST':
        if form.is_valid():
            car_request = form.save(commit=False)
            car_request.user = user
            car_request.save()

            return redirect('d_index',user_id)

@login_required
def view_single_ride(request,carsharing_id):
    carsharing = CarSharing.objects.get(pk=carsharing_id)

    return render(request, 'vehicle/view_one_ride.html', {"carsharing":carsharing})

@login_required
def view_single_vehicle(reuqest,carsharing_id):
    carsharing = CarDetails.objects.get(pk=carsharing_id)
    return render(request, 'vehicle/view_car.html', {"carsharing":carsharing})
