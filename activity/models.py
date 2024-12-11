from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Atividade(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    projeto = models.CharField(max_length=255)
    atividade = models.CharField(max_length=255)
    funcionarios = models.CharField(max_length=255)
    controle = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.projeto} - {self.atividade}"
