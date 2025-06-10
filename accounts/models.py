from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    EDUCATION_CHOICES = [
        ('highschool', 'High School'),
        ('associate', 'Associate Degree'),
        ('bachelor', 'Bachelor\'s Degree'),
        ('master', 'Master\'s Degree'),
        ('phd', 'PhD'),
    ]
    
    email = models.EmailField(unique=True)
    pfp = models.ImageField(
        upload_to='profile_pics/', 
        blank=True, 
        null=True,
        default = "profile_pics/default.png")
    max_education = models.CharField(
        max_length=20,
        choices=EDUCATION_CHOICES,
        blank=True,
        null=True,
        default = "highschool"
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email