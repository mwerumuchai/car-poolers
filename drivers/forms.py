from django import forms
from .models import Profile,Request,CarSharing
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic','website', 'bio', 'location', 'phone_number','sex')

        exclude = ['comment',]

class RequestRideForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('destination','pick_up_point')

class CarSharingForm(forms.ModelForm):
    class Meta:
        model = CarSharing
        fields =('start','destination','start_time','arrival_time')
