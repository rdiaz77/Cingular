from django.urls import path
from . import views

# purchase_orders
# purchase_orders/1/details

app_name = 'order'

urlpatterns = [
    path("", views.index, name= 'index'),
    path('<int:order_id>', views.detail, name = 'detail')
    
]
