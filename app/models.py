from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    PET_CHOICES = (
        ('DOG', 'Dog'),
        ('CAT', 'Cat')
    )

    type_pet = models.CharField(max_length=3, choices=PET_CHOICES, default='Dog')
    birthday = models.DateField()
