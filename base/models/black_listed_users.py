from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BlacklistedUser(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)