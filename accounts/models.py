from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (("MANAGER", "MANAGER"), ("USER", "USER"))

    first_name = None
    last_name = None

    nickname = models.CharField(max_length=20, blank=False)
    role = models.CharField(max_length=7, default="USER")

    def __str__(self):
        return self.nickname
