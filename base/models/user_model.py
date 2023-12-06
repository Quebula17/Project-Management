from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True, null=True)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(null=True)
    current_year = models.IntegerField(null=True)

    password = models.CharField(max_length=128, default=make_password('password'))

    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username} ({'admin' if self.is_admin else 'not admin'})"