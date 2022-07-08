from django.db import models
from bookings.models import HotelDetails

class PayScale(models.Model):
    designation = models.CharField(max_length=255, primary_key=True)
    basic_pay = models.BigIntegerField()
    HRA = models.BigIntegerField()
    TA = models.BigIntegerField()
    MA = models.BigIntegerField()
    PF = models.BigIntegerField()
    gross_pay = models.BigIntegerField()
    net_pay = models.BigIntegerField()


class EmployeeDetails(models.Model):
    employee_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(HotelDetails, to_field='hotel_id',on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    designation = models.ForeignKey(PayScale, to_field='designation',on_delete=models.CASCADE)
    experience = models.IntegerField(default=0)
    address = models.CharField(max_length=400, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    pin = models.CharField(max_length=255, null=True)
    contact_no = models.CharField(max_length=10, null=True)
    aadhaar_no = models.CharField(max_length=16, null=True)


class IncrementDetails(models.Model):
    increment_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(EmployeeDetails, to_field='employee_id',on_delete=models.CASCADE)


