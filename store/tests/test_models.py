from django.test import TestCase

from django.contrib.auth.models import User
from store.models import *

class TestCategoriesModel(TestCase):

    def setUp(self): # INFORMACION QUE VOY A CARGAR  PARA TESTEAR
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self): # PRUEBA DE CARGAR LA INFORMACION EN LOS MODELOS A TESTEAR
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category)) # REALIZA EL TESTEO 

    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):
    def setUp(self): # ¿Que tengo que tener para probar un producto? Una categoria, un producto, un usuario
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1, slug='django-beginners', price='20.00', image='')

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')