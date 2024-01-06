import json
import requests
from config import public_key



url_oc = f"https://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?codigo=1627-1836-SE23&ticket={
    public_key}"

response_oc = requests.get(url_oc).json()  # converts json to dict
# print(response_oc)
data_oc = response_oc["Listado"]
# print(data_oc)

for item in data_oc:
    # print(item["Fechas"])
    # print(item["TotalNeto"])
    # print(item["Comprador"])
    provider_oc = (item["Proveedor"])
    # print(item["Items"])
    buyer_oc = (item["Comprador"])

print(buyer_oc["RutUnidad"])
print(provider_oc["Codigo"])


# Datos consulta: Cantidad, FechaCreacion, Version // response_oc
# Datos OC: 'Codigo', 'CodigoEstado', CodigTipo, Codigo, CodigoEstadoProveedor, 'TipoMoneda','FechaAceptacion', 'FechaCancelacion',TotalNeto, 'PorcentajeIva','Impuestos','Total',Financiamiento'
# Comprador: 'CodigoOrganismo','CodigoUnidad', "ComunaUnidad",RegionUnidad
# Proveedor: Codigo, Comuna, Region
# Items : Cantidad, Correlativo, CodigoProducto, EspecificacionComprador, EspecificacionProveedor, Cantidad, Unidad, Moneda, PrecioNeto, TotalCargos, TotalDescuentos,TotalDescuentos, Total.

# for item in orden_compra:
#     print(item["Codigo"])
# [item for item in list]
