from django.shortcuts import render
from django. shortcuts import get_object_or_404

from django.http import JsonResponse

from .basket import Basket
from store.models import Product

def basket_summary(request):
    return render(request, 'store/basket/summary.html')

def basket_add(request): #COLLECT DATA QUE NOS ENVIO JQUERY DESDE ADD BASKET
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid')) # RECUPERA EL PRODUCT ID DEL SCRIPT DE JS EN EL TEMPLATE (id=productid)
        product_qty = int(request.POST.get('productqty')) # RECUPERA EL PRODUCTQTY DEL SCRIPT DE JS EN EL TEMPLATE (id=productqty)
        product = get_object_or_404(Product, id=product_id) # retrieves the product data from the database
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({ # LA VARIABLE RESPONSE ES UN ARCHIVO JSON PARA QUE PUEDA UTILIZARLO EL NAVEGADOR EN EL JS
            'qty': basketqty
        })

        return response # devuelve el archivo JSON