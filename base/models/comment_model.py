from django.db import models
from base.models.card_model import Card
from base.models.user_model import User

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='comments')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_comments')
    contents = models.TextField()

    def __str__(self):
        return f"Comment {self.comment_id} on {self.card.heading}"