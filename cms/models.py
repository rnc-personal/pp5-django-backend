from django.db import models
from django.contrib.auth.models import User
from builds.models import Build

class FeaturedBuilder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class HeroContent(models.Model):
    heading = models.CharField(max_length=255)
    paragraph_text = models.TextField()

    def __str__(self):
        return f"{self.heading} | {self.paragraph} "

class FeaturedBuild(models.Model):
    build = models.ForeignKey(Build, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.build)