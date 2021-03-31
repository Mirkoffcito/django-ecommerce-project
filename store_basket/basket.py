from decimal import Decimal
from store.models import Product

class Basket(): # SI EL USUARIO NO TIENE UNA SESION EXISTENTE, SE CREA UNA NUEVA Y SE LE ASIGNA UN SKEY
    """
    A base basket class, providing some default behaviours that can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        
        self.session = request.session # PIDE INFORMACIÓN SOBRE LA SESION INICIADA Y LA ALMACENA EN SELF.SESSION
        basket = self.session.get('skey') # SESSION KEY UNICA
        if 'skey' not in request.session:
            basket = self.session['skey'] = {'number': 1231231}
        self.basket = basket

    def add(self, product, qty):
        """
        Adding and updating the users basket session data
        """
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {'price':str(product.price), 'qty':int(qty)}
        
        self.save()

    def __len__(self):
        """
        Gets the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values()) #retorna sumatoria de las cantidades de todos los items en el carrito

    def save(self):
        self.session.modified = True