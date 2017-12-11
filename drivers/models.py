from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
import datetime as dt
from random import choices
import string as str

class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255, blank=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to = 'driverphotos/',blank=True)
    # cardetails = models.ForeignKey(CarDetails, on_delete=models.CASCADE)


    User.profile = property(lambda u: DriverProfile.objects.get_or_create(user=u)[0])

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:

        DriverProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    instance.profile.save()

def generate_id():
        n = 10
        random = str.ascii_uppercase + str.ascii_lowercase + str.digits
        return ''.join(choice(random) for _ in range(n))

class CarDetails(models.Model):
    make_of_car = models.CharField(max_length=255, blank=False)
    plates_number = models.CharField(max_length=10, blank=False)
    car_model = models.CharField(max_length=255, blank=False)
    color = models.CharField(max_length=10,blank=False)
    no_of_seats = models.IntegerField(blank=False)
    picture = models.ImageField(upload_to = 'driverphotos/',blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.make_of_car + " " + self.car_model + " belonging to " + self.user.username


class CarSharing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.CharField(max_length=255, blank=False, )
    destination = models.CharField(max_length=255, blank=False)
    cost = models.IntegerField(blank=False)
    post_date = models.DateTimeField(auto_now_add = True)
    start_time = models.TimeField(max_length=255, blank=False)
    arrival_time = models.TimeField(max_length=255, blank=False)
    no_passengers = models.IntegerField(blank=False)
    ride_details = models.TextField(blank=False)
    cardetails = models.ForeignKey(CarDetails, on_delete=models.CASCADE)
    sharing_ended = models.BooleanField(default=False)

    def __str__(self):
        return self.start + " to " + self.destination

    def get_user(self):
        return self.user


class Request(models.Model):
    carsharing = models.ForeignKey(CarSharing, on_delete=models.CASCADE)
    pick_up_point = models.CharField(max_length=255, blank=False, )
    destination = models.CharField(max_length=255, blank=False)
    register_date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estimated_cost = models.IntegerField(blank=False)
    status = models.CharField(max_length=255, blank=False, default='pending')

    def __str__(self):
        return self.pick_up_point

# class DriverProfile(models.Model):
#     driver = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_pic = models.ImageField('photos/', blank=False)
#     current_location = models.CharField(max_length=100, blank=False)
#     destination = models.CharField(max_length=100,blank=False)
