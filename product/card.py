from .models import Product

class Card:

    def __init__(self,request):
        self.session=request.session

        card=self.session.get('session_key')

        if 'session_key' not in request.session:
            card=self.session['session_key']={}

        self.card=card

    def add(self,product,quantity):
        product_id=str(product.id)

        if product_id in self.card:
            pass
        else:
            self.card[product_id]=str(quantity)


        self.session.modified=True

    def __len__(self):
        return len(self.card)
    

    def get_product(self):
        product_ids=self.card.keys()

        product=Product.objects.filter(id__in=product_ids)
        return product
    
    def get_quantity(self):

        quantity=self.card

        return quantity
    
    def get_totol_price(self):
        product_ids=self.card.keys()
        products=Product.objects.filter(id__in=product_ids)
        totol=0
        for key,value in self.card.items():
            key=int(key)
            for product in products:
                if product.id==key:
                    totol+=(product.price*int(value))
                    
        return totol
    def get__price(self):
           pass
    
    def delete_product(self,product_id):
        product_id=str(product_id)
        if product_id in self.card:
            del self.card[product_id]


        self.session.modified=True

    def product_update(self,product,quantity):
        product_id=str(product.id)
        quantity=int(quantity)
        if quantity<=0:
            raise ValueError('musbat son kiriting')
        else:
            self.card[product_id]=quantity
            self.session.modified=True

        card=self.card
        
        return card