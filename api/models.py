from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE_CHOICE = (
        ('admin','Admin'),
        ('premium','Premium'),
        ('simple','Simple')
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICE,default='simple')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
