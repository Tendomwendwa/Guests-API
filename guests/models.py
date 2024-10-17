from django.db import models

# Create your models here.
class Guest (models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Male')
    address = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.name}"