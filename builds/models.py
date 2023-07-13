from django.db import models
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
    build_cpu = models.CharField(max_length=255, choices=CPU_CHOICES)
    build_mobo = models.CharField(max_length=255, choices=MOBO_CHOICES)
    build_ram = models.CharField(max_length=255, choices=RAM_CHOICES)
    build_disk = models.CharField(max_length=255, choices=DISK_CHOICES)
    build_gpu = models.CharField(max_length=255, choices=GPU_CHOICES)
    build_case = models.CharField(max_length=255, choices=CASE_CHOICES)
    build_monitor = models.CharField(max_length=255, choices=MONITOR_CHOICES)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.build_name}'
