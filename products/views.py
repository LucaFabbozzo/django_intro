from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all().values()
    # #con .filter() possiamo attivare un piccolo filtro passandogli come argomento quello che vorrei far ritornare
    # productos = Product.objects.filter(puntaje=3)
    # #se voglio una cosa in particolare devo utilizzare get() in questo caso ad esempio primary key = 3
    # productos = Product.objects.get(pk=3)
    #print(products)

    #JsonResponse funziona soltanto con dati che corrispondano a dizionari
    #bisogna quindi cambiare il tipo di dato in una lista con list()
    return JsonResponse(list(products), safe=False)


#questo caso è utilizzato soltanto se si vuole utilizzare un prototipo rapido e se si vuole costruire qualcosa di serio meglio utilizzare una dipendenza di terzi