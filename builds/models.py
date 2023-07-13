from django.db import models
from django.contrib.auth.models import User


class Build(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    build_name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )

    build_cpu = models.CharField(max_length=255, choices=CPU_CHOICES)
    build_mobo = models.Charfield(max_length=255, choices=MOBO_CHOICES)
    build_ram = models.CharField(max_length=255, choices=RAM_CHOICES)
    build_disk = models.CharField(max_length=255, choices=DISK_CHOICES)
    build_gpu = models.CharField(max_length=255, choices=GPU_CHOICES)
    build_case = models.CharField(max_length=255, choices=CASE_CHOICES)
    build_monitor = models.CharField(max_length=255, choices=MONITOR_CHOICES)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'