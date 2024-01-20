from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100 , help_text='Nome da Empresa')

    def __str__(self):
        return self.nome

