from decimal import Decimal
from django.conf import settings
from productproject.models import Plate


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, plate, quantity=1, update_quantity=False):
        plate_id = str(plate.id)

        if plate_id not in self.cart:
            self.cart[plate_id] = {'quantity': 0, 'price': str(plate.price)}

        if update_quantity:
            self.cart[plate_id]['quantity'] = quantity
        else:
            self.cart[plate_id]['quantity'] += quantity

        self.save()

    def remove(self, plate):
        plate_id = str(plate.id)
        if plate_id in self.cart:
            del self.cart[plate_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def __iter__(self):
        plate_ids = self.cart.keys()
        plates = Plate.objects.filter(id__in=plate_ids)
        cart = self.cart.copy()

        for plate in plates:
            cart[str(plate.id)]['plate'] = plate

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        if settings.CART_SESSION_ID in self.session:
            del self.session[settings.CART_SESSION_ID]
            self.session.modified = True
            self.cart = {}