from .models import Category_product
from .card import Card


def categoriya(request):
    return {'categories':Category_product.objects.all()}

def card_funk(request):
    return {"card":Card(request)}