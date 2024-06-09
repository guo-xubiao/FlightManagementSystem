from django.contrib import admin
from .models import Flight, Passenger, Booking

admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Booking)
