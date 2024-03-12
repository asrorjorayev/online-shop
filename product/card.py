
class Card:

    def __init__(self,request):
        self.session=request.session

        card=self.session.get('session_key')

        if 'session_key' not in request.session:
            card=self.session['session_key']={}

        self.card=card

    def add(self,product):
        product_id=str(product.id)

        if product_id in self.card:
            pass
        else:
            self.card[product_id]=str(product.price)


        self.session.modified=True

    def __len__(self):
        return len(self.card)