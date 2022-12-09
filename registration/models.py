from django.db import models
from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)
    confirm_email_address = models.EmailField(max_length=100)
    phone_number = PhoneNumberField(max_length=100)
    create_password = models.CharField(max_length=100)
    retype_password = models.CharField(max_length=100)

def __str__(self):
    return self.first_name + ' ' + self.last_name
