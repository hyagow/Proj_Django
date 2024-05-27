from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Definir o texto que aparecereçá (em vez de 'Categoria object' """
        return self.nome


class Transacao(models.Model):
    data = models.DateTimeField()  # auto_now=True | auto_now_add=True
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # A transacao vai poder ter 1 Categoria, mas a Categoria pode estar em varias transacoes
    observacoes = models.TextField(null=True, blank=True)  # campo de texto

    class Meta:
        verbose_name_plural = 'Transações'

    def __str__(self):
        """ Definir o texto que aparecereçá (em vez de 'Transacao object' """
        return self.descricao

# Os relacionamentos de BD são basicamente 3:
# - ForeignKey        => 1 -> m
# - OneToOneField     => 1 -> 1
# - ManytoManyField   => m -> m

# Após a criação de um modelo:
# - python3 manage.py makemigrations    => Criar o arquivo de migração
# - python3 manage.py migrate           => Aplicar a criação da nova tabela no BD
# - Registar o novo model em admin.py
    # from .models import Transacao
    # admin.site.register(Transacao)
