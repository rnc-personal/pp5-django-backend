from django.db import models
from django.contrib.auth.models import User
from builds.models import Build
from django.core.validators import MaxValueValidator

class Rating(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    build = models.ForeignKey(Build, related_name='ratings', on_delete=models.CASCADE)
    score = models.FloatField(default=0, validators=[MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['creator', 'build']

    def __str__(self):
        return f"{self.creator} rated {self.build} {self.score}/10"

    def save(self, *args, **kwargs):
            super(Rating, self).save(*args, **kwargs)
            self.build.save()