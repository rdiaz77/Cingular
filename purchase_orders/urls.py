from django.urls import path
from . import views

# purchase_orders
# purchase_orders/1/details

urlpatterns = [
    path("", views.index, name= "order_index"),
    path('<int:order_id>', views.detail, name = 'order_detail')
    
]
