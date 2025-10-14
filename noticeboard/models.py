from django.db import models
from django.contrib.auth.models import User
from produtos.models import Empregos
from django.utils import timezone
# Create your models here.
class NoticeBoarforUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Empregos, on_delete=models.CASCADE)
    approvedselection = models.BooleanField(default=False)
    rh_observation = models.TextField(verbose_name="Descrição do Canditatos", max_length=300, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.title
