from django.db import models
from django.contrib.auth.models import User
from builds.models import Build
from django.core.validators import MaxValueValidator

class Rating(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    build = models.ForeignKey(Build, related_name='rating', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['creator', 'build']

    def __str__(self):
        return f"{self.creator} rated {self.post} {self.rating}/10"