from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from builds.components import CPU_CHOICES, MOBO_CHOICES, RAM_CHOICES, DISK_CHOICES, GPU_CHOICES, CASE_CHOICES, MONITOR_CHOICES

class Build(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    build_name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='images/', default='../default_build_nvxeo7')
    gallery_image_1 = models.ImageField(upload_to='images/', default='../default_build_nvxeo7')
    gallery_image_2 = models.ImageField(upload_to='images/', default='../default_build_nvxeo7')
    gallery_image_3 = models.ImageField(upload_to='images/', default='../default_build_nvxeo7')
    gallery_image_4 = models.ImageField(upload_to='images/', default='../default_build_nvxeo7')
    build_cpu = models.CharField(max_length=255)
    build_mobo = models.CharField(max_length=255,)
    build_ram = models.CharField(max_length=255)
    build_disk = models.CharField(max_length=255,)
    build_gpu = models.CharField(max_length=255)
    build_case = models.CharField(max_length=255)
    build_monitor = models.CharField(max_length=255)
    user_rating_1 = models.ManyToManyField(User, related_name='user_rating_1', blank=True, editable=False)
    ratings_count = models.IntegerField(default=0)
    average_rating = models.DecimalField(max_digits=2, decimal_places=2, default=0)

    def average_rating_1(self):
        return self.user_rating_1.aggregate()


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.build_name}'


