from django.db import models
from django.utils import timezone

# Create your models here.
# Datos consulta: Cantidad, FechaCreacion, Version // response_oc
# Datos OC: 'Codigo', 'CodigoEstado', CodigTipo, Codigo, CodigoEstadoProveedor, 'TipoMoneda','FechaAceptacion', 'FechaCancelacion',TotalNeto, 'PorcentajeIva','Impuestos','Total',Financiamiento'
# Comprador: 'CodigoOrganismo','CodigoUnidad', "ComunaUnidad",RegionUnidad
# Proveedor: Codigo, Comuna, Region
# Items : Cantidad, Correlativo, CodigoProducto, EspecificacionComprador, EspecificacionProveedor, Cantidad, Unidad, Moneda, PrecioNeto, TotalCargos, TotalDescuentos,TotalDescuentos, Total.

class Orders(models.Model):
    number = models.CharField(max_length=255)
    status_code = models.IntegerField()
    name = models.CharField(max_length=255)
    tender_code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    creation_date = models.DateField()
    aceptance_date = models.DateField()
    cancelation_date = models.DateField()
    payment_terms = models.CharField(max_length=255)
    net_total = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)
   

class Buyer(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    oc_number = models.ForeignKey(Orders, on_delete=models.CASCADE)

class Seller(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    oc_number = models.ForeignKey(Orders, on_delete=models.CASCADE)

class Product(models.Model):
    description = models.CharField(max_length=255)
    oc_number = models.ForeignKey(Orders, on_delete=models.CASCADE)

