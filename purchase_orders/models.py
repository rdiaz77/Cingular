from django.db import models
from django.utils import timezone

# Create your models here.
# Datos consulta: Cantidad, FechaCreacion, Version // response_oc
# Datos OC: 'Codigo', 'CodigoEstado', CodigTipo, Codigo, CodigoEstadoProveedor, 'TipoMoneda','FechaAceptacion', 'FechaCancelacion',TotalNeto, 'PorcentajeIva','Impuestos','Total',Financiamiento'
# Comprador: 'CodigoOrganismo','CodigoUnidad','NombreUnidad', "ComunaUnidad",RegionUnidad
# Proveedor: Codigo, Comuna, Region
# Items : Cantidad, Correlativo, CodigoProducto, EspecificacionComprador, EspecificacionProveedor, Cantidad, Unidad, Moneda, PrecioNeto, TotalCargos, TotalDescuentos,TotalDescuentos, Total.

class Orders(models.Model):
    number = models.CharField(max_length=255)
    status_code = models.IntegerField()
    name = models.CharField(max_length=255)
    # tender_code = models.CharField(max_length=255)
    # description = models.CharField(max_length=255)
    # type = models.CharField(max_length=255)
    # currency = models.CharField(max_length=255)
    # seller_status = models.IntegerField()
    # creation_date = models.DateField()
    # acceptance_date = models.DateField()
    # cancelation_date = models.DateField()
    # has_products = models.CharField(max_length=2)
    # has_dscto = models.FloatField()
    # has_charges = models.FloatField()
    # net_total = models.FloatField()
    # has_taxes = models.FloatField()
    # total = models.FloatField()
    # payment_terms = models.CharField(max_length=255)
    # date_created = models.DateTimeField(default=timezone.now)
   
# Comprador: 'CodigoUnidad','NombreUnidad', "ComunaUnidad",RegionUnidad

class Buyer(models.Model):
    buyer_code = models.CharField(max_length=255)
    buyer_name = models.CharField(max_length=255)
    buyer_rut = models.CharField(max_length=20)
    buyer_unit_name = models.CharField(max_length=255)
    buyer_city = models.CharField(max_length=255)
    buyer_region = models.CharField(max_length=255)
    oc_number = models.ForeignKey(Orders, on_delete=models.CASCADE)

class Seller(models.Model):
    seller_code = models.IntegerField()
    seller_name = models.CharField(max_length=255)
    seller_rut = models.CharField(max_length=20)
    seller_city = models.CharField(max_length=255)
    seller_region = models.CharField(max_length=255)
    oc_number = models.ForeignKey(Orders, on_delete=models.CASCADE)

class Product(models.Model):
    product_total = models.IntegerField()
    product_description = models.CharField(max_length=255)
    product_sequence = models.IntegerField()
    product_code_category = models.IntegerField()
    product_b_specs = models.CharField(max_length=510)
    product_s_specs = models.CharField(max_length=510)
    product_quatity = models.FloatField()
    product_net_price = models.FloatField()
    product_total_charges = models.FloatField()
    product_total_dscto = models.FloatField()
    product_total_taxes = models.FloatField()
    product_total = models.FloatField()
    oc_number = models.ForeignKey(Orders, on_delete=models.CASCADE)

