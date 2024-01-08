from django.contrib import admin
from .models import Orders

# Register your models here.

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_code', 'name')




admin.site.register(Orders,OrdersAdmin)