from django.db import models
from django.core.validators import validate_email

import phonenumbers
from django.core.exceptions import ValidationError

# Create your models here.


class date(models.Model):
    date = models.DateField()

class destination(models.Model):
    description= models.TextField()
    image = models.ImageField(upload_to='static/', null=True)
   


class appointment(models.Model):
    
    first_name = models.CharField(    max_length=30)
    last_name = models.CharField(max_length=30)
    age=models.IntegerField()   
    date = models.DateField()
    sex = models.CharField(max_length=1, choices=[('M', 'Male'),('F', 'Female'), ])
    email = models.EmailField(validators=[validate_email])
    phone_number = models.CharField(max_length=20)

    def clean(self):
        try:
            parsed_number = phonenumbers.parse(self.phone_number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                raise ValidationError("Invalid phone number")
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValidationError("Invalid phone number")
