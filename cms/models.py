from django.db import models
from django.contrib.auth.models import User
from builds.models import Build

class HeroContent(models.Model):
    heading = models.CharField(max_length=255)
    paragraph_text = models.TextField()

    def __str__(self):
        return f"{self.heading} | {self.paragraph_text} "
