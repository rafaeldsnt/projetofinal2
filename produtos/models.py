from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
JOB_TYPE = (("0", "Selecione uma opção"), ("1", "CLT - 8  horas"), ("2", "Consultoria - 8 horas"))

class Empregos(models.Model):
    title = models.CharField(max_length=300, verbose_name="Título da vaga" )
    description = models.TextField(verbose_name="Descrição da vaga")
    location = models.CharField(max_length=150)
    job_option = models.CharField(
            max_length=10,
            choices=JOB_TYPE,
            default='0',
        )
    category = models.CharField(max_length=100)
    last_date = models.DateField()
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
        return  f"job_option: {self.get_job_option_display()}"

