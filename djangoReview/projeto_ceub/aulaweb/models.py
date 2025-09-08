from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao=models.DateTimeField(auto_now=True)

    class Meta:
        db_table="produto"
        ordering=["nome"]
        verbose_name="Produto"
        verbose_name_plural="Produto"

    def __str__(self):
        return f"{self.nome} - R${self.preco}"
    
# Create your models here.
