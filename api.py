import json
import requests
from config import public_key



url_oc = f"https://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?codigo=1627-1836-SE23&ticket={
    public_key}"

d = requests.get(url_oc).json()


d_oc = d["Listado"][0]

# 'FechaCreacion': '2023-12-01T10:41:02.777', 'FechaEnvio': '2023-12-13T10:37:18.837', 'FechaAceptacion': '2023-12-13T19:23:24.39', 'FechaCancelacion': None, 'FechaUltimaModificacion': '2023-12-14T16:38:00'}
d_date = d["Listado"][0]["Fechas"]

# {'CodigoOrganismo': '7448', 'NombreOrganismo': 'SERVICIO DE SALUD HOSPITAL DE SAN FERNANDO', 'RutUnidad': '61.602.145-1', 'CodigoUnidad': '2623', 'NombreUnidad': 'Hospital de San Fernando Abastecimiento', 'Actividad': 'HOSPITALES Y CLINICAS', 'DireccionUnidad': 'Negrete 1401', 'ComunaUnidad': 'San Fernando', 'RegionUnidad': 'Región del Libertador General Bernardo O´Higgins', 'Pais': 'CL', 'NombreContacto': 'Giovanni Gonzalez', 'CargoContacto': 'Administrativo Logistica', 'FonoContacto': '', 'MailContacto': ''}

d_buyer = d["Listado"][0]["Comprador"]


# {'CodigoOrganismo': '7448', 'NombreOrganismo': 'SERVICIO DE SALUD HOSPITAL DE SAN FERNANDO', 'RutUnidad': '61.602.145-1', 'CodigoUnidad': '2623', 'NombreUnidad': 'Hospital de San Fernando Abastecimiento', 'Actividad': 'HOSPITALES Y CLINICAS', 'DireccionUnidad': 'Negrete 1401', 'ComunaUnidad': 'San Fernando', 'RegionUnidad': 'Región del Libertador General Bernardo O´Higgins', 'Pais': 'CL', 'NombreContacto': 'Giovanni Gonzalez', 'CargoContacto': 'Administrativo Logistica', 'FonoContacto': '', 'MailContacto': ''}
d_seller = d["Listado"][0]["Proveedor"]


# 'Cantidad': 3, 'Listado': [{'Correlativo': 1, 'CodigoCategoria': 41116000, 'Categoria': 'Equipamiento para laboratorios / Instrumentos de medida y experimentación / Reactivos de analizadores clínicos y diagnósticos', 'CodigoProducto': 41116004, 'Producto': 'Reactivos de analizadores químicos', 'EspecificacionComprador': 'REACTIVO PARA DETERMINACIÓN DE NIVELES DE AMIKACINA (R1 2X19ML R2: 2X7 ML)\r\n', 'EspecificacionProveedor': 'REACTIVO PARA DETERMINACIÓN DE NIVELES DE AMIKACINA (R1 2X19ML R2: 2X7 ML)', 'Cantidad': 1.0, 'Unidad': None, 'Moneda': 'CLP', 'PrecioNeto': 899500.0, 'TotalCargos': 0.0, 'TotalDescuentos': 0.0, 'TotalImpuestos': 0.0, 'Total': 899500.0}, {'Correlativo': 2, 'CodigoCategoria': 41116000, 'Categoria': 'Equipamiento para laboratorios / Instrumentos de medida y experimentación / Reactivos de analizadores clínicos y diagnósticos', 'CodigoProducto': 41116004, 'Producto': 'Reactivos de analizadores químicos', 'EspecificacionComprador': 'TIRAS REACTIVAS PARA DETERMINACIÓN DE CETONEMIA (B-KETONE)(50 DETERMINACIONES C/U)', 'EspecificacionProveedor': 'TIRAS REACTIVAS PARA DETERMINACIÓN DE CETONEMIA (B-KETONE)(50 DETERMINACIONES C/U)', 'Cantidad': 4.0, 'Unidad': None, 'Moneda': 'CLP', 'PrecioNeto': 357500.0, 'TotalCargos': 0.0, 'TotalDescuentos': 0.0, 'TotalImpuestos': 0.0, 'Total': 1430000.0}, {'Correlativo': 3, 'CodigoCategoria': 41116000, 'Categoria': 'Equipamiento para laboratorios / Instrumentos de medida y experimentación / Reactivos de analizadores clínicos y diagnósticos', 'CodigoProducto': 41116004, 'Producto': 'Reactivos de analizadores químicos', 'EspecificacionComprador': 'CALIBRADOR PARA TÉCNICA AMIKACINA ( 6 NOVELES, 1X1 ML CADA UNO)', 'EspecificacionProveedor': 'CALIBRADOR PARA TÉCNICA AMIKACINA ( 6 NOVELES, 1X1 ML CADA UNO)', 'Cantidad': 1.0, 'Unidad': None, 'Moneda': 'CLP', 'PrecioNeto': 340000.0, 'TotalCargos': 0.0, 'TotalDescuentos': 0.0, 'TotalImpuestos': 0.0, 'Total': 340000.0}]}

d_items = d["Listado"][0]["Items"]
d_items_details = d["Listado"][0]["Items"]["Listado"][1]["PrecioNeto"]
print(d_items_details)

# for item in data_oc:
    # print(item["Fechas"])
    # print(item["TotalNeto"])
    # print(item["Comprador"])
    # provider_oc = (item["Proveedor"])
    # # print(item["Items"])
    # buyer_oc = (item["Comprador"])



# Datos consulta: Cantidad, FechaCreacion, Version // response_oc
# Datos OC: 'Codigo', 'CodigoEstado', CodigTipo, Codigo, CodigoEstadoProveedor, 'TipoMoneda','FechaAceptacion', 'FechaCancelacion',TotalNeto, 'PorcentajeIva','Impuestos','Total',Financiamiento'
# Comprador: 'CodigoOrganismo','CodigoUnidad', "ComunaUnidad",RegionUnidad
# Proveedor: Codigo, Comuna, Region
# Items : Cantidad, Correlativo, CodigoProducto, EspecificacionComprador, EspecificacionProveedor, Cantidad, Unidad, Moneda, PrecioNeto, TotalCargos, TotalDescuentos,TotalDescuentos, Total.


# d = requests.get("http://ergast.com/api/f1/2019/drivers.json")
# d = d.json()
# print(d)
# drivers = d["MRData"]["DriverTable"]["Drivers"]
# print(f'this is drivers {drivers}')