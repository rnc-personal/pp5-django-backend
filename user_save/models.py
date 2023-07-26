from django.db import models
from django.contrib.auth.models import User
from builds.models import Build

class Save(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    build = models.ForeignKey(Build, related_name='saves', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['creator', 'build']

    def __str__(self):
        return f"{self.creator} saved {self.build}"
    