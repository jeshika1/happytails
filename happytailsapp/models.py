from datetime import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# Create your models here.
User = get_user_model()
from django.db import models

class Animal(models.Model):
    category= models.CharField(max_length=255, default='street')
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='animals/')

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class addyours(models.Model):
      PET_STATUS_CHOICES = [
        ('vaccinated', 'Vaccinated'),
        ('notVaccinated', 'Not Vaccinated'),
        ('Unknown', 'Unknown'),
      ]
      petImage= models.ImageField(upload_to='uploads/')
      petName=  models.TextField()
      petWeight =  models.TextField()
      petBreed =  models.TextField()
      vaccinationStatus = models.CharField(
        max_length=15,
        choices=PET_STATUS_CHOICES,
        default='Unknown',
      )

      


class AdoptionApplication(models.Model):
    # Personal Information
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)  # Assuming a simple representation for a phone number
    email = models.EmailField()

    # Household Information
    RESIDENCE_TYPES = [
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('condo', 'Condo'),
        # Add more options if necessary
    ]
    residenceType = models.CharField(max_length=20, choices=RESIDENCE_TYPES)

    # Pet Care Information
    exercisePlan = models.TextField()
    hoursAlone = models.PositiveIntegerField()
    previousPets = models.TextField()
    

    # Additional Fields
    # Add more fields as needed
    

    
class Process(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('denied', 'Denied'),
    ]
    # other fields for the order
    pet = models.ForeignKey(AdoptionApplication, on_delete=models.CASCADE, default="")  # Assuming you have a Pet model
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

     