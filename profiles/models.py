from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

    COUNTRY_CHOICES = [
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('MX', 'Mexico'),
        ('AU', 'Australia'),
        ('GB', 'United Kingdom'),
        ('DE', 'Germany'),
        ('FR', 'France'),
        ('ES', 'Spain'),
        ('IT', 'Italy'),
        ('JP', 'Japan'),
        ('CN', 'China'),
        ('KR', 'South Korea'),
        ('AU', 'Australia'),
    ]


    creator = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, choices=COUNTRY_CHOICES)
    description = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    profile_image = models.ImageField(
        upload_to='images/',
        default='../default_profile_qlt6oa.png'
    )

    profile_banner = models.ImageField(
        upload_to='images/',
        default='../default-banner_jzvnux'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.creator}'s profile"

# Function for creating a profile, when a new user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(creator=instance)

# This is a signal to watch for a new user registering 
# It will then create a profile 
post_save.connect(create_profile, sender=User)
