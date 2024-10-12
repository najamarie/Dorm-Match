from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    SUFFIX_CHOICES = [
        ('Jr', 'Jr.'),
        ('Sr', 'Sr.'),
        ('II', 'II'),
        ('III', 'III'),
    ]
    
    GENDER_CHOICES = [
        ('Cisgender Female', 'Cisgender Female'),
        ('Cisgender Male', 'Cisgender Male'),
        ('Transgender Male', 'Transgender Male'),
        ('Transgender Female', 'Transgender Female'),
        ('Non-Binary', 'Non-Binary'),
    ]
    
    username = models.CharField(max_length=255, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    suffix = models.CharField(max_length=10, choices=SUFFIX_CHOICES, blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    degree_program = models.CharField(max_length=100)