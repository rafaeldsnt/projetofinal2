from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
JOB_TYPE = (("1", "CLT - 8  horas"), ("2", "Consultoria - 8 horas"))

class Empregos(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    location = models.CharField(max_length=150)
    type_job = models.CharField(choices=JOB_TYPE, default="1", max_length=10)
    category = models.CharField(max_length=100)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    website = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)
    salary = models.IntegerField(default=0, blank=True)
    vacancy = models.IntegerField(default=1)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title

