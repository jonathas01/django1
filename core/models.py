from django.db import models

class Produto(models.Model): 
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField("Quantidade em estoque")
    
    def __str__(self) -> str:
        return self.nome
    
class Cliente(models.Model):
        nome = models.CharField('Nome', max_length=100)
        sobrenome = models.CharField('Sobrenome', max_length= 100)
        email = models.EmailField("Email", max_length=254)
        
        def __str__(self) -> str:
             return self.nome