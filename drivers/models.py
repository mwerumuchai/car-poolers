from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
import datetime as dt
from random import choice
import string as str

# Gender_Choices = (
#     ('male','Male'),
#     ('female' 'Female'),
#     ('not_specified' 'Not Specified'),
# )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField()
    phone_number = PhoneNumberField(max_length=10, blank=True)
    # gender = models.CharField(max_length=30, choices=Gender_Choices, default='None', blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to = 'photos/',blank=True)


    User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:

        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    instance.profile.save()

def generate_id():
        n = 10
        random = str.ascii_uppercase + str.ascii_lowercase + str.digits
        return ''.join(choice(random) for _ in range(n))
