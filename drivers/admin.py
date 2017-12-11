from django.contrib import admin
from .models import DriverProfile,CarDetails,CarSharing,Request

admin.site.register(DriverProfile)
admin.site.register(CarDetails)
admin.site.register(CarSharing)
admin.site.register(Request)

# Register your models here.
