from django import forms
from .models import RiderProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = RiderProfile
        fields = ('profile_pic', 'bio', 'location', 'phone_number')

        exclude = ['comment',]
