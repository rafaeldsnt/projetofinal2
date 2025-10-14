from django.db import models
from django.contrib.auth.models import User
from produtos.models import Empregos
from django.utils import timezone


APPROVED_CHOICES = [("0", "Selecione uma opção"), ("1", "Aprovado"), ("2", "Rejeitado")]

# Create your models here.
class HRdecision(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Empregos, on_delete=models.CASCADE)
    candidate_observation = models.TextField(verbose_name="Descrição do Canditatos", max_length=300, null=True)
    rh_decision = models.CharField(max_length=10,choices=APPROVED_CHOICES, default='0',  null=True, verbose_name="Decisão da Aprovação")
    rh_observation = models.TextField(verbose_name="Descrição", max_length=300, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.title
