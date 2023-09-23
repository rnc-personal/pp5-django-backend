from django.db import models
from django.contrib.auth.models import User
from builds.models import Build
from django.core.validators import MaxValueValidator, MinValueValidator

class Comments(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    build = models.ForeignKey(Build, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

class Ratings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    build = models.ForeignKey(Build, on_delete=models.CASCADE)
    rating_value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('user', 'build')
        ordering = ['-rating_value']

    def __str__(self):
        return f"{self.user} rated {self.build} with score of {self.rating_value} "
