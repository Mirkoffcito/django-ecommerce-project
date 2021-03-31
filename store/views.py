from django.shortcuts import render, get_object_or_404
from .models import *

def index(self):
    pass


def products_allActive(request):
    products = Product.products.all() # query de la base de datos para obtener todos los productos
    context = {
        'products': products
    }
    return render(request, 'store/home.html', context) # STORE/HOME.HTML EN REALIDAD ES TEMPLATES/STORE/HTML, PERO LA PRIMER PARTE ESTÁ ACLARADA EN SETTINGS

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True) # SI EL PRODUCTO ESTÁ EN STOCK, LO MUESTRA. ASGINA A SLUG EL SLUG RECUPERADO EN LAS URL
    context = {
        'product': product
    }
    return render(request, 'store/products/detail.html', context)

def category_list(request, category_slug): # devuelve los productos de una sola categoria al template
    category = get_object_or_404(Category, slug=category_slug) #RECUPERA EL SLUG DE LA CATEGORIA Y LA GUARDA EN SLUG
    products = Product.products.filter(category=category) # QUERY DE LA CATEGORIA ELEGIDA
    context = { # VARIABLES PARA USAR EN LOS TEMPLATES
        'category': category, # CATEGORIA
        'products': products # PRODUCTOS DEL QUERY DE LA CATEGORIA
    }
    return render(request, 'store/products/category.html', context) # DEVUELVE AL TEMPLATE


