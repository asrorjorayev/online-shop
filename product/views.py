from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Product,Category_product
from django.http import HttpResponse,JsonResponse
from .card import Card

# def index(request):
#     return render(request,'index.html')

# class ProductListWiev(ListView):
#     cat=Category_product.objects.all()
#     model =Product
#     template_name='index.html'
#     context_object_name='products'
#     extre_context={
#         "categories":cat
#         }

def index(request):
    products = Product.objects.all()

    data = {
        'products':products,
    }
    return render(request, "index.html", context=data)

def category(request,id):
    categories = Category_product.objects.all()
    cat=get_object_or_404(Category_product,pk=id)
    product=cat.products.all()
    data={
        'categories':categories,
        'products':product
    }
    return render(request,'category.html',context=data)


class ProductDteailViev(DetailView):
    model=Product
    template_name='detail.html'
    context_object_name='product'

def card_summary(request):
    return HttpResponse('salom')

def card_add(request):
    card=Card(request)
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        product=get_object_or_404(Product,id=product_id)

        card.add(product=product)

        return JsonResponse({"product_id":str(product_id)})


    return HttpResponse('salom')

def card_update(request):
    return HttpResponse('salom')

def card_delete(request):
    return HttpResponse('salom')
