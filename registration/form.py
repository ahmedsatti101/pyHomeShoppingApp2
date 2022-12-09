from django import forms
from django.forms import ModelForm
from .models import Customer
from phonenumber_field.formfields import PhoneNumberField

class Customerform(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            "Create password" : forms.PasswordInput(attrs={'placeholder' : '********', 'autocomplete' : 'off','data-toggle' : 'password'}),
        }