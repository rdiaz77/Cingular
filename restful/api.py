import json
import requests


# from cingular.config import public_key


url_oc = "https://api.mercadopublico.cl/servicios/v1/publico/ordenesdecompra.json?codigo=1627-1836-SE23&ticket=F8537A18-6766-4DEF-9E59-426B4FEE2844"


def fecthData():
    res = requests.get(url_oc).json()
    print(res)

# entrega la full lista de informacion, aunque el dict base que genera json tiene informacion addicional:
# Cantidad': 1, 'FechaCreacion': '2024-01-07T05:22:48.0319247Z', 'Version': 'v1'
# {'Codigo': '1627-1836-SE23', 'Nombre': 'CINTAS DE CETONEMIA', 'CodigoEstado': 12, 'Estado': 'Recepción Conforme', 'CodigoLicitacion': '', 'Descripcion': 'SE REQUIERE PARA EL LABORATORIO DEL HOSPITAL DE SAN FERNANDO\r\n\r\nSBYS 1345\r\n\r\nSEGÚN COT N°2544', 'CodigoTipo': '8', 'Tipo': 'SE', 'TipoMoneda': 'CLP', 'CodigoEstadoProveedor': 7, 'EstadoProveedor': 'Recepción Conforme', 'Fechas': {'FechaCreacion': '2023-12-01T10:41:02.777', 'FechaEnvio': '2023-12-13T10:37:18.837', 'FechaAceptacion': '2023-12-13T19:23:24.39', 'FechaCancelacion': None, 'FechaUltimaModificacion': '2023-12-14T16:38:00


list = res["Listado"][0]

def ocData():
    for oc in list:
        oc_num = list['Codigo']
        oc_status= list['CodigoEstado']
        oc_name= list['Nombre']
    return(oc_num, oc_status, oc_name)

# #  Insert data in sqlite
# # for dr in drivers:
# #     name = dr["familyName"]
# #     number = dr["permanentNumber"] 
# #     sql = 'INSERT INTO Drivers (name,number) VALUES(?,?)'
# #     val = (name,number)
# #     cur.execute(sql,val)


# # 'FechaCreacion': '2023-12-01T10:41:02.777', 'FechaEnvio': '2023-12-13T10:37:18.837', 'FechaAceptacion': '2023-12-13T19:23:24.39', 'FechaCancelacion': None, 'FechaUltimaModificacion': '2023-12-14T16:38:00'}

# res_date = res["Listado"][0]["Fechas"]

# for i in res_date:
#     f_creation = res_date['FechaCreacion']
#     if res_date['FechaCancelacion'] != None:
#         f_cancela = res_date['FechaCancelacion']
#     else:
#         f_cancela = "empty"

# print(f_cancela)
# print(f_creation)


# # {'CodigoOrganismo': '7448', 'NombreOrganismo':, 'RutUnidad': '61.602.145-1', 'CodigoUnidad': '2623', 'NombreUnidad': 'Hospital de San Fernando Abastecimiento', 'Actividad': 'HOSPITALES Y CLINICAS', 'DireccionUnidad': 'Negrete 1401', 'ComunaUnidad': 'San Fernando', 'RegionUnidad': 'Región del Libertador General Bernardo O´Higgins', 'Pais': 'CL', 'NombreContacto': 'Giovanni Gonzalez', 'CargoContacto': 'Administrativo Logistica', 'FonoContacto': '', 'MailContacto': ''}

# res_buyer = res["Listado"][0]["Comprador"]


# # {'CodigoOrganismo': '7448', 'NombreOrganismo': 'SERVICIO DE SALUD HOSPITAL DE SAN FERNANDO', 'RutUnidad': '61.602.145-1', 'CodigoUnidad': '2623', 'NombreUnidad': 'Hospital de San Fernando Abastecimiento', 'Actividad': 'HOSPITALES Y CLINICAS', 'DireccionUnidad': 'Negrete 1401', 'ComunaUnidad': 'San Fernando', 'RegionUnidad': 'Región del Libertador General Bernardo O´Higgins', 'Pais': 'CL', 'NombreContacto': 'Giovanni Gonzalez', 'CargoContacto': 'Administrativo Logistica', 'FonoContacto': '', 'MailContacto': ''}

# res_seller = res["Listado"][0]["Proveedor"]


# # 'Cantidad': 3, 'Listado': [{'Correlativo': 1, 'CodigoCategoria': 41116000, 'Categoria': 'Equipamiento para laboratorios / Instrumentos de medida y experimentación / Reactivos de analizadores clínicos y diagnósticos', 'CodigoProducto': 41116004, 'Producto': 'Reactivos de analizadores químicos', 'EspecificacionComprador': 'REACTIVO PARA DETERMINACIÓN DE NIVELES DE AMIKACINA (R1 2X19ML R2: 2X7 ML)\r\n', 'EspecificacionProveedor': 'REACTIVO PARA DETERMINACIÓN DE NIVELES DE AMIKACINA (R1 2X19ML R2: 2X7 ML)', 'Cantidad': 1.0, 'Unidad': None, 'Moneda': 'CLP', 'PrecioNeto': 899500.0, 'TotalCargos': 0.0, 'TotalDescuentos': 0.0, 'TotalImpuestos': 0.0, 'Total': 899500.0}, {'Correlativo': 2, 'CodigoCategoria': 41116000, 'Categoria': 'Equipamiento para laboratorios / Instrumentos de medida y experimentación / Reactivos de analizadores clínicos y diagnósticos', 'CodigoProducto': 41116004, 'Producto': 'Reactivos de analizadores químicos', 'EspecificacionComprador': 'TIRAS REACTIVAS PARA DETERMINACIÓN DE CETONEMIA (B-KETONE)(50 DETERMINACIONES C/U)', 'EspecificacionProveedor': 'TIRAS REACTIVAS PARA DETERMINACIÓN DE CETONEMIA (B-KETONE)(50 DETERMINACIONES C/U)', 'Cantidad': 4.0, 'Unidad': None, 'Moneda': 'CLP', 'PrecioNeto': 357500.0, 'TotalCargos': 0.0, 'TotalDescuentos': 0.0, 'TotalImpuestos': 0.0, 'Total': 1430000.0}, {'Correlativo': 3, 'CodigoCategoria': 41116000, 'Categoria': 'Equipamiento para laboratorios / Instrumentos de medida y experimentación / Reactivos de analizadores clínicos y diagnósticos', 'CodigoProducto': 41116004, 'Producto': 'Reactivos de analizadores químicos', 'EspecificacionComprador': 'CALIBRADOR PARA TÉCNICA AMIKACINA ( 6 NOVELES, 1X1 ML CADA UNO)', 'EspecificacionProveedor': 'CALIBRADOR PARA TÉCNICA AMIKACINA ( 6 NOVELES, 1X1 ML CADA UNO)', 'Cantidad': 1.0, 'Unidad': None, 'Moneda': 'CLP', 'PrecioNeto': 340000.0, 'TotalCargos': 0.0, 'TotalDescuentos': 0.0, 'TotalImpuestos': 0.0, 'Total': 340000.0}]}

# res_items = res["Listado"][0]["Items"]
# res_items_details = res["Listado"][0]["Items"]["Listado"][1]["PrecioNeto"]
# # print(d)





