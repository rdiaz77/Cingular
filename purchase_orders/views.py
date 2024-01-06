from django.shortcuts import render
from django.http import HttpResponse
from purchase_orders.models import Orders, Buyer, Seller, Product



# Create your views here.


def index(request):
    orders = Orders.objects.all()
    # output = ", ".join([oc.name for oc in orders])
    # return HttpResponse('hola')
    # return HttpResponse(output)
    return render(request, 'orders/index.html', {'orders': orders})
    
    

    

