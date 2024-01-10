from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    score = models.FloatField()
    #CASCADE: elimina il prodotto se si elimina la categoria
    #PROTECT: lancia un errore non mi lascia eliminare la categoria
    #RESTRICT: solo elimina se non esistono prodotti
    #SET_NULL: valore nullo se si attualizza la categoria
    #SET_DEFAULT: assegna un valore per defetto
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE
    )
    #aggiungo un'altra colonna voglio che in automatico mi crea la data di creazione 
    create_at = models.DateTimeField(default=timezone.now)
