from django.db import models
from django import forms


class GuestDetails(models.Model):
    user_name = models.CharField(primary_key=True, max_length=255)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    adhaar_no = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name