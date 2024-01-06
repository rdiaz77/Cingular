from django.shortcuts import render
from django.http import HttpResponse
from purchase_orders.models import Orders, Buyer, Seller, Product



# Create your views here.


def index(request):
    response = Orders.objects.all()
    output = ", ".join([oc.name for oc in response])
    # return HttpResponse('hola')
    return HttpResponse(output)
    
    

    

