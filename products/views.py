from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product


# def index(request):
#     products = Product.objects.all().values()

#     #JsonResponse funziona soltanto con dati che corrispondano a dizionari
#     #bisogna quindi cambiare il tipo di dato in una lista con list()

#     return JsonResponse(list(products), safe=False)

# #questo caso è utilizzato soltanto se si vuole utilizzare un prototipo rapido e se si vuole costruire qualcosa di serio meglio utilizzare una dipendenza di terzi



#funzioni per poter utilizzare il template di Django
def index(request):
    products = Product.objects.all()

    return render(
        request,
        'index.html',
        context={'products': products}
    )


def detail(request, product_id):
    product = Product.objects.get(id=product_id)


    return render(
        request,
        'detalle.html',
        context={'product': product}
    )