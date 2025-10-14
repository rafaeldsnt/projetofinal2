from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ResumeCv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Nome do usuário" )
    name = models.CharField(max_length=255,  verbose_name="Nome Completo")
    email = models.EmailField(max_length=35, verbose_name="E-mail")
    celphone = models.CharField(max_length=20, verbose_name="Telefone de contato")
    city = models.CharField(max_length=50, verbose_name="Cidade de Residencia")
    adress_user = models.CharField(max_length=50, default="", verbose_name="Informe o seu Endereço completo")
    state = models.CharField(max_length=50, verbose_name="Estado")
    qualifications = models.TextField(null=True, blank=True, verbose_name="Informe sua Escolaridade")
    courses = models.TextField(null=True, blank=True, verbose_name="Quais as tecnologias que vc conhece ?")
    experiences = models.TextField(null=True, blank=True, verbose_name="Informe suas Experiências anteriores")
    resume_file = models.FileField(upload_to='documents/', default='documents/default.txt', verbose_name="Realize o upload do seu Curriculum Vitae")
    is_published = models.BooleanField(default=True, verbose_name="O curriculum é valido ?")
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.name