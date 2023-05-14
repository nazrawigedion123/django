from django import forms
from . import models
from .models import destination, appointment
from django.core.files.storage import DefaultStorage
from django.core.files.storage import FileSystemStorage
from pathlib import Path
import os





class DestinationForm(forms.ModelForm):
    class Meta:
        model = destination
        fields = ['image', 'description']


class ContactForm1(forms.Form):
     
    description = forms.CharField(max_length=100)


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = appointment
        
        fields = ['first_name', 
                  'last_name',
                  'age',
                  'date',
                  'sex',
                  'email',
                  'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
            'sex': forms.Select(attrs={'placeholder': 'Sex'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),


        }
        
   


    