from django.db import models


class categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nome


class produto(models.Model):
    nome = models.CharField(max_length=100)
    preço = models.IntegerField()
    descrição = models.TextField()
    categoria = models.ForeignKey(categoria, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome
