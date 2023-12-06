from django.db import models
from base.models.list_model import List
from django.contrib.auth import get_user_model

User = get_user_model()

class Card(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_title = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    assigned_users = models.ManyToManyField(User, related_name='cards')
    task_list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='cards')
    description = models.TextField()

    def __str__(self):
        return self.heading