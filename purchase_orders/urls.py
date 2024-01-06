from django.urls import path
from . import views

# purchase_orders
# purchase_orders/1/details
urlpatterns = [
    path("", views.index, name= "index")
    
]
