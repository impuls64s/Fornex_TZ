from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    balance = models.FloatField(default=0.0)
    is_verified = models.BooleanField(default=False)
