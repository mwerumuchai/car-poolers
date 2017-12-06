from __future__ import absolute_import
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction
from django.http import Http404
from .forms import UserForm,ProfileForm
from .models import RiderProfile
import datetime as dt
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse

# Create your views here.
@login_required(login_url='/accounts/register/')
def r_index(request):
    return render(request, 'riders/r-index.html')

def logout(request):
    return render(request, 'riders/r-index.html')

def about(request):
    return render(request, 'about.html')

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
            return redirect('riders:profiles')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'riders/profiles/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def profile(request,username):
    try:
        user = User.objects.get(username=username)
        profile_pic = RiderProfile.objects.filter(user_id=user).all().order_by('-id')
    except ObjectDoesNotExist:
        raise Http404()

    return render(request, 'riders/profiles/profile.html', {"user":user, "profile_pic":profile_pic})
