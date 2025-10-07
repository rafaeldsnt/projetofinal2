from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
JOB_TYPE = [("0", "Selecione uma opção"), ("1", "CLT - 8  horas"), ("2", "Consultoria - 8 horas")]


class SpecialtyDefendant(models.Model):
    identificacao = models.CharField(max_length=100, 
        verbose_name="Título da Especialidade", )
    
    descricao = models.TextField (
        verbose_name="Descrição da Especialidade",
        max_length=200
    )
    
    def __str__(self):
        return self.identificacao

class Empregos(models.Model):
    title = models.CharField(max_length=300, verbose_name="Título da vaga")
    description = models.TextField(verbose_name="Descrição da vaga")
    location = models.CharField(max_length=150, verbose_name="Atuação da Vaga/Remoto ou Local")
    job_option = models.CharField(max_length=10,choices=JOB_TYPE, default='0', verbose_name="Tipo de contratação")
    category = models.CharField(max_length=100, verbose_name="Atuação da Vaga")
    last_date = models.DateTimeField(verbose_name="Data de Postagem da Vaga", blank=False)
    company_name = models.CharField(max_length=100, verbose_name="Empresa Solicitante")
    company_description = models.CharField(max_length=300, verbose_name="Atuação da Empresa Solicitante")
    website = models.CharField(max_length=100, default="", verbose_name="Web Site da Empresa Solicitante")
    created_at = models.DateTimeField(auto_now_add=True)
    filled = models.BooleanField(default=True, verbose_name="Vaga está ativa ?")
    salary = models.IntegerField(default=0, blank=True, verbose_name="Salario proposto ?")
    vacancy = models.IntegerField(default=1, verbose_name="Quantidade de Vagas propostas ?")
    specialtydefendant = models.ManyToManyField (SpecialtyDefendant,related_name="specialty_defendant")

    class Meta:
        ordering = ["id"]

    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
    
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Empregos, on_delete=models.CASCADE, related_name="favorites")
    created_at = models.DateTimeField(default=timezone.now)
    soft_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.job.title

