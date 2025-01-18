from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (("MANAGER", "MANAGER"), ("USER", "USER"))

    first_name = None
    last_name = None

    username_validator = RegexValidator(
        r"^[a-zA-Z0-9_ ]+$",  # 알파벳, 숫자, _(under score), 공백만 허용
        message="알파벳, 숫자, _(언더스코어), 공백만 허용됩니다.",
    )

    username = models.CharField(
        max_length=20, blank=False, unique=True, validators=[username_validator]
    )
    nickname = models.CharField(max_length=20, blank=False)
    role = models.CharField(max_length=7, default="USER")

    def __str__(self):
        return self.nickname
