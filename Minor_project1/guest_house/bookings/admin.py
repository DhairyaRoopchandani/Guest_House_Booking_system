from django.contrib import admin
from .models import *

admin.site.register(HotelDetails)
admin.site.register(RoomPriceDetails)
admin.site.register(DiscountDetails)
admin.site.register(RoomDetails)
admin.site.register(DiscountAvailed)
admin.site.register(BookingDetails)