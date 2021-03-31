from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True) # Nombre de la categoría
    slug = models.SlugField(max_length=255, unique=True) # parte de la dirección URL

    class Meta:
        verbose_name_plural = 'Categories' # para que django no ponga nombre "categorys"

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug]) # STORE(NOMBRE DE LA APP):PRODUCT_DETAIL(NOMBRE DEL PATH), LE PASAMOS EL SLUG

    def __str__(self):
        return self.name
        

class ProductManager(models.Manager): # CUSTOM MANAGER PARA QUERYSETS DE PRODUCTOS SOLO ACTIVOS
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE) # no puede haber productos sin categoría
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager() # DEFAULT MANAGER PARA HACER QUERYS
    products = ProductManager() # CUSTOM MANAGER DEFINIDO PARA QUERYS DE LOS PRODUCTOS SOLO ACTIVOS

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)# ORDENA EN LA BASE DE DATOS POR EL MOMENTO EN EL QUE FUE CREADO EL PRODUCTO

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug]) # STORE(NOMBRE DE LA APP):PRODUCT_DETAIL(NOMBRE DEL PATH), LE PASAMOS EL SLUG
    
    def __str__(self):
        return self.title
    
    
