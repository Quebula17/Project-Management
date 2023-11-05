from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True, null=True)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(null=True)
    enrollment_number = models.IntegerField(blank=True, null=True)
    current_year = models.IntegerField(null=True)

    password = models.CharField(max_length=255, null=True, blank=True)

    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username} ({'admin' if self.is_admin else 'not admin'})"