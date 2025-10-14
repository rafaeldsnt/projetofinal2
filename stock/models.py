from django.db import models
from django.contrib.auth.models import User
from produtos.models import Empregos
from django.utils import timezone
# Create your models here.

class StockGeneralJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Empregos, on_delete=models.CASCADE)
    preview = models.IntegerField(default=0)
    closure = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user
