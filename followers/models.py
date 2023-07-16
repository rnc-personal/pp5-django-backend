from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
    creator = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['creator', 'followed']

    def __str__(self):
        return f'{self.creator.username} is following {self.followed.username}'