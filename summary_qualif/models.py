from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ResumeCv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=35)
    celphone = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    qualifications = models.TextField(null=True, blank=True)
    courses = models.TextField(null=True, blank=True)
    experiences = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name