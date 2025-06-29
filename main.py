# main.py
from fastapi import FastAPI
from datetime import datetime
import pytz
from fastapi.middleware.cors import CORSMiddleware
from core.company import company_directa, company_list_DZ, company_list_grupo_1, company_list_grupo_2, company_list_grupo_3, company_list_solo_DZ, company_single
from core.controller import get_defaul_xss_data
from core.helpers import custom_transform
from core.query import documentos_entregas_tiempo_excedido, documentos_ventas_tiempo_excedido, query_GDD_report, query_catalogo_solo_dz, query_catalogo_solo_pronaca, query_clave_usuario, query_clientes_nuevos, query_clientes_nuevos_ruta, query_cobros_diarios, query_cobros_diarios_no_ruta_fecha, query_cobros_diarios_si_procesados, query_cobros_diarios_si_ruta_fecha, query_detalle_cliente_nuevo_pedido, query_detalle_devolucion_cliente_fecha, query_detalle_diario, query_detalle_diario_por_rutas, query_detalle_pedido_cliente_fecha, query_detalle_pedido_directa, query_detalle_pedido_dmd_code, query_general_dia, query_informacion_entrega, query_licencias_activas, query_matriz_gdd_pollo_blanco, query_matriz_gdd_pollo_criollo, query_retornos, query_retornos_no_procesados_ruta_fecha, query_retornos_si_procesados_ruta_fecha, query_rev_day, query_rev_dia_directa, query_rutas_por_sincronizar, query_sincronizacion_rutas, query_sincronizo_mas_de_una_vez, query_solo_stock_dz_dia, query_status_total_parcial_10_min, query_stock_dz, query_ultimos_pedidos
import core.constantes as const


# Crea una instancia de la aplicación FastAPI
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/home_api/')
def home_api():
    dt = datetime.now()
    localtime = dt.astimezone (pytz.timezone('America/Guayaquil'))
    localtime = localtime.strftime ("%Y-%m-%d")
    return {"message": "Hello PanchisioApi", "Job":"Is Work...!", "Time":datetime.now(),
            "Endpoints":[
                "====",
                "== REVISIONES MAÑANA ==",
                "====",
                f"{const.HOST}/home_api/stock_directa",
                f"{const.HOST}/home_api/matriz_pollo_blanco_directa",
                f"{const.HOST}/home_api/matriz_pollo_criollo_directa",
                f"{const.HOST}/home_api/general_dia_directa",
                f"{const.HOST}/home_api/stock_grupo_1",
                f"{const.HOST}/home_api/matriz_pollo_blanco_grupo_1",
                f"{const.HOST}/home_api/matriz_pollo_criollo_grupo_1",
                f"{const.HOST}/home_api/general_dia_grupo_1",
                f"{const.HOST}/home_api/stock_grupo_2",
                f"{const.HOST}/home_api/matriz_pollo_blanco_grupo_2",
                f"{const.HOST}/home_api/matriz_pollo_criollo_grupo_2",
                f"{const.HOST}/home_api/general_dia_grupo_2",
                f"{const.HOST}/home_api/stock_grupo_3",
                f"{const.HOST}/home_api/matriz_pollo_blanco_grupo_3",
                f"{const.HOST}/home_api/matriz_pollo_criollo_grupo_3",
                f"{const.HOST}/home_api/general_dia_grupo_3",
                f"{const.HOST}/home_api/stock_solo_grupo_1",
                f"{const.HOST}/home_api/stock_solo_grupo_2",
                f"{const.HOST}/home_api/stock_solo_grupo_3",
                f"{const.HOST}/home_api/rev_day_company/CENACOP",
                f"{const.HOST}/home_api/licencias_activas",
                f"{const.HOST}/home_api/catalogo_por_dz/CENACOP/0101",
                f"{const.HOST}/home_api/catalogo_solo_directa/0101",
                f"{const.HOST}/home_api/catalogo_todos_dz/'0101'",
                f"{const.HOST}/home_api/gdd_report/{localtime}/?doc=0",
                f"{const.HOST}/home_api/gdd_report_company/PRONACA/{localtime}",
                f"{const.HOST}/home_api/usuario_clave/PRONACA/T1143",
                "====",
                "== FTP ==",
                f"{const.HOST}/home_api/ftp_pronaca_status" ,
                f"{const.HOST}/home_api/ftp_3am_status" ,
                f"{const.HOST}/home_api/ftp_4am1_status" ,
                f"{const.HOST}/home_api/ftp_4am2_status",
                "====",
                "== REVISIONES TARDE ==",
                "====",
                f"{const.HOST}/home_api/clientes_nuevos/madeli/{localtime}",
                f"{const.HOST}/home_api/clientes_nuevos_ruta_fecha/madeli/300/{localtime}",
                f"{const.HOST}/home_api/detalle_diario/madeli/{localtime}",
                f"{const.HOST}/home_api/detalle_diario_todos/{localtime}",
                f"{const.HOST}/home_api/detalle_diario_ruta/madeli/{localtime}",
                f"{const.HOST}/home_api/parcial_total_10_all",
                f"{const.HOST}/home_api/rutas_por_sincronizar/PRONACA/{localtime}",
                f"{const.HOST}/home_api/sincronizacion_rutas/PRONACA",
                f"{const.HOST}/home_api/sincronizo_mas_una_vez_todos",
                f"{const.HOST}/home_api/rutas_por_sincronizar_dz_grupo_1/{localtime}",
                f"{const.HOST}/home_api/rutas_por_sincronizar_dz_grupo_2/{localtime}",
                f"{const.HOST}/home_api/rutas_por_sincronizar_dz_grupo_3/{localtime}",
                f"{const.HOST}/home_api/actualizacion_cliente/madeli/{localtime}",
                f"{const.HOST}/home_api/detalle_diario_directa/PRONACA/{localtime}",
                f"{const.HOST}/home_api/documentos_ventas_exceden/PRONACA/{localtime}/10",
                f"{const.HOST}/home_api/documentos_entregas_exceden/PRONACA/{localtime}/10",
                "====",                
                f"=== COBROS ===",
                "====",
                f"{const.HOST}/home_api/cobros_diarios_no_procesados/PRONACA/{localtime}",
                f"{const.HOST}/home_api/cobros_diarios_si_procesados/PRONACA/{localtime}",
                f"{const.HOST}/home_api/cobros_diarios_no_procesados_r_f/PRONACA/828/{localtime}",
                f"{const.HOST}/home_api/cobros_diarios_si_procesados_r_f/PRONACA/828/{localtime}",
                "====",
                f"=== PEDIDO DETALLE PEDIDDO ===",
                f"{const.HOST}/home_api/ultimos_pedidos/PRONACA/cliente",
                f"{const.HOST}/home_api/detalle_pedido_cliente_fecha/PRONACA/cliente/{localtime}",
                f"{const.HOST}/home_api/detalle_pedido_dmd_code/PRONACA/dmd_code",
                f"{const.HOST}/home_api/detalle_dev_cliente_fecha/PRONACA/cliente/{localtime}",
                f"{const.HOST}/home_api/cliente_nuevo_pedido/PRONACA/{localtime}",
                "====",                
                f"=== ENTREGAS ===",
                "====",
                f"{const.HOST}/home_api/retornos_no_procesados/PRONACA/{localtime}",
                f"{const.HOST}/home_api/retornos_no_procesados_r_f/PRONACA/T2120/{localtime}",
                f"{const.HOST}/home_api/retornos_si_procesados_r_f/PRONACA/T2120/{localtime}",
                f"{const.HOST}/home_api/informacion_entrega/PRONACA/T1143",]}



@app.get("/")
def read_root():
    """
    Este endpoint devuelve la hora actual en la zona horaria de Ecuador
    y un mensaje de estado del servidor.
    """
    # Define la zona horaria de Ecuador
    ecuador_tz = pytz.timezone('America/Guayaquil')
    
    # Obtiene la hora actual y la formatea
    hora_actual_ecuador = datetime.now(ecuador_tz).strftime("%Y-%m-%d %H:%M:%S %Z")
    
    return {
        "hora_actual": hora_actual_ecuador,
        "estado_servidor": "is running"
    }

#GRUPO 1

@app.get('/home_api/stock_grupo_1')
async def stock_grupo_1():
    data_ = get_defaul_xss_data(company_list_grupo_1(), query_stock_dz())
    data = custom_transform(data_)
    return data

@app.get('/home_api/matriz_pollo_blanco_grupo_1')
async def matriz_pollo_blanco_grupo_1():
    data_ = get_defaul_xss_data(company_list_grupo_1(), query_matriz_gdd_pollo_blanco())
    data = custom_transform(data_)
    return data

@app.get('/home_api/matriz_pollo_criollo_grupo_1')
async def matriz_pollo_criollo_grupo_1():
    data_ = get_defaul_xss_data(company_list_grupo_1(), query_matriz_gdd_pollo_criollo())
    data = custom_transform(data_)
    return data

@app.get('/home_api/general_dia_grupo_1')
async def general_dia_grupo_1():
    data_ = get_defaul_xss_data(company_list_grupo_1(), query_general_dia())
    data = custom_transform(data_)
    return data


#GRUPO 2

@app.get('/home_api/stock_grupo_2')
async def stock_grupo_2():
    data_ = get_defaul_xss_data(company_list_grupo_2(), query_stock_dz())
    data = custom_transform(data_)
    return data

@app.get('/home_api/matriz_pollo_blanco_grupo_2')
async def matriz_pollo_blanco_grupo_2():
    data_ = get_defaul_xss_data(company_list_grupo_2(), query_matriz_gdd_pollo_blanco())
    data = custom_transform(data_)
    return data

@app.get('/home_api/matriz_pollo_criollo_grupo_2')
async def matriz_pollo_criollo_grupo_2():
    data_ = get_defaul_xss_data(company_list_grupo_2(), query_matriz_gdd_pollo_criollo())
    data = custom_transform(data_)
    return data

@app.get('/home_api/general_dia_grupo_2')
async def general_dia_grupo_2():
    data_ = get_defaul_xss_data(company_list_grupo_2(), query_general_dia())
    data = custom_transform(data_)
    return data


#GRUPO 3

@app.get('/home_api/stock_grupo_3')
async def stock_grupo_3():
    data_ = get_defaul_xss_data(company_list_grupo_3(), query_stock_dz())
    data = custom_transform(data_)
    return data

@app.get('/home_api/matriz_pollo_blanco_grupo_3')
async def matriz_pollo_blanco_grupo_3():
    data_ = get_defaul_xss_data(company_list_grupo_3(), query_matriz_gdd_pollo_blanco())
    data = custom_transform(data_)
    return data

@app.get('/home_api/matriz_pollo_criollo_grupo_3')
async def matriz_pollo_criollo_grupo_3():
    data_ = get_defaul_xss_data(company_list_grupo_3(), query_matriz_gdd_pollo_criollo())
    data = custom_transform(data_)
    return data

@app.get('/home_api/general_dia_grupo_3')
async def general_dia_grupo_3():
    data_ = get_defaul_xss_data(company_list_grupo_3(), query_general_dia())
    data = custom_transform(data_)
    return data

#SOLO STOCK DZ

@app.get('/home_api/stock_solo_grupo_1')
async def stock_solo_grupo_1():
    data_ = get_defaul_xss_data(company_list_grupo_1(), query_solo_stock_dz_dia())
    data = custom_transform(data_)
    return data

@app.get('/home_api/stock_solo_grupo_2')
async def stock_solo_grupo_2():
    data_ = get_defaul_xss_data(company_list_grupo_2(), query_solo_stock_dz_dia())
    data = custom_transform(data_)
    return data

@app.get('/home_api/stock_solo_grupo_3')
async def stock_solo_grupo_3():
    data_ = get_defaul_xss_data(company_list_grupo_3(), query_solo_stock_dz_dia())
    data = custom_transform(data_)
    return data


#DIRECTA
@app.get('/home_api/stock_directa/')
async def stock_directa():
    return get_defaul_xss_data(company_directa(), query_rev_dia_directa())



@app.get('/home_api/matriz_pollo_blanco_directa')
async def matriz_pollo_blanco_directa():
    data_ = get_defaul_xss_data(company_directa(), query_matriz_gdd_pollo_blanco())
    data = custom_transform(data_)
    return data

@app.get('/home_api/matriz_pollo_criollo_directa')
async def matriz_pollo_criollo_directa():
    data_ = get_defaul_xss_data(company_directa(), query_matriz_gdd_pollo_criollo())
    data = custom_transform(data_)
    return data

@app.get('/home_api/general_dia_directa')
async def general_dia_directa():
    data_ = get_defaul_xss_data(company_directa(), query_general_dia())
    data = custom_transform(data_)
    return data



@app.get('/home_api/rev_day_company/{company_name}')
async def rev_day_company(company_name: str):
    #comp = company_single(name=company_name.upper())
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_rev_day())

@app.get('/home_api/catalogo_por_dz/{company_name}/{item}')
async def catalogo_por_dz(company_name: str, item: str):
    #comp = company_single(name=company_name.upper())
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_catalogo_solo_dz(item))

@app.get('/home_api/catalogo_solo_directa/{item}')
async def catalogo_solo_directa(item: str):
    #comp = company_single(name=company_name.upper())
    return get_defaul_xss_data(company_directa(), query_catalogo_solo_pronaca(item))


@app.get('/home_api/catalogo_todos_dz/{item}')
async def catalogo_todos_dz(item: str):
    data_ = get_defaul_xss_data(company_list_solo_DZ(), query_catalogo_solo_dz(item))
    data = custom_transform(data_)
    return data

#GDD SUBIR
@app.get('/home_api/gdd_report/{date}')
async def gdd_report(date: str, doc: int = 0):
    return get_defaul_xss_data(company_list_DZ(), query_GDD_report(date),doc)

@app.get('/home_api/gdd_report_company/{company_name}/{date}')
async def gdd_report_company(company_name: str, date: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_GDD_report(date))



@app.get('/home_api/licencias_activas')
async def licencias_activas():
    data_ = get_defaul_xss_data(company_list_DZ(), query_licencias_activas())
    data = custom_transform(data_)
    return data


@app.get('/home_api/usuario_clave/{company_name}/{ruta}')
async def usuario_clave(company_name: str, ruta: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_clave_usuario(ruta))

#retornos

@app.get('/home_api/retornos_no_procesados/{company_name}/{fecha}')
async def retornos_no_procesados(company_name: str, fecha: str):
    #comp = company_single(name=company_name.upper())
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_retornos(fecha))

@app.get('/home_api/retornos_no_procesados_r_f/{company_name}/{ruta}/{fecha}')
async def retornos_no_procesados_r_f(company_name: str, ruta: str, fecha: str):
    #comp = company_single(name=company_name.upper())
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_retornos_no_procesados_ruta_fecha(ruta, fecha))

@app.get('/home_api/retornos_si_procesados_r_f/{company_name}/{ruta}/{fecha}')
async def retornos_si_procesados_r_f(company_name: str, ruta: str, fecha: str):
    #comp = company_single(name=company_name.upper())
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_retornos_si_procesados_ruta_fecha(ruta, fecha))

#cobros

@app.get('/home_api/cobros_diarios_no_procesados/{company_name}/{fecha}')
async def cobros_diarios_no_procesados(company_name: str, fecha: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_cobros_diarios(fecha))


@app.get('/home_api/cobros_diarios_si_procesados/{company_name}/{fecha}')
async def cobros_diarios_si_procesados(company_name: str, fecha: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_cobros_diarios_si_procesados(fecha))


@app.get('/home_api/cobros_diarios_no_procesados_r_f/{company_name}/{ruta}/{fecha}')
async def cobros_diarios_no_procesados_r_f(company_name: str, ruta: str, fecha: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_cobros_diarios_no_ruta_fecha(ruta, fecha))


@app.get('/home_api/cobros_diarios_si_procesados_r_f/{company_name}/{ruta}/{fecha}')
async def cobros_diarios_si_procesados_r_f(company_name: str, ruta: str, fecha: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_cobros_diarios_si_ruta_fecha(ruta, fecha))

###

@app.get('/home_api/rutas_por_sincronizar/{company_name}/{fecha}')
async def rutas_por_sincronizar(company_name: str, fecha: str):
    #comp = company_single(name=company_name.upper())
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_rutas_por_sincronizar(fecha))


@app.get('/home_api/sincronizacion_rutas/{company_name}')
async def sincronizacion_rutas(company_name: str):
    #comp = company_single(name=company_name.upper())
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_sincronizacion_rutas())


@app.get('/home_api/informacion_entrega/{company_name}/{ruta}')
async def informacion_entrega(company_name: str, ruta: str):
    #comp = company_single(name=company_name.upper())
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_informacion_entrega(ruta))

#DETALLE PEDIDOS
@app.get('/home_api/ultimos_pedidos/{company_name}/{cliente}')
async def ultimos_pedidos(company_name: str, cliente: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_ultimos_pedidos(cliente))

@app.get('/home_api/detalle_pedido_cliente_fecha/{company_name}/{cliente}/{fecha}')
async def detalle_pedido_cliente_fecha(company_name: str, cliente: str, fecha: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_detalle_pedido_cliente_fecha(cliente, fecha))


@app.get('/home_api/detalle_pedido_dmd_code/{company_name}/{dmd_code}')
async def detalle_pedido_dmd_code(company_name: str, dmd_code: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_detalle_pedido_dmd_code(dmd_code))


@app.get('/home_api/detalle_dev_cliente_fecha/{company_name}/{cliente}/{fecha}')
async def detalle_dev_cliente_fecha(company_name: str, cliente: str, fecha: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_detalle_devolucion_cliente_fecha(cliente, fecha))

@app.get('/home_api/cliente_nuevo_pedido/{company_name}/{fecha}')
async def cliente_nuevo_pedido(company_name: str, fecha: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_detalle_cliente_nuevo_pedido(fecha))




@app.get('/home_api/detalle_diario_directa/{company_name}/{fecha}')
async def detalle_pedido_dmd_code(company_name: str, fecha: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_detalle_pedido_directa(fecha))

@app.get('/home_api/detalle_diario_ruta/{company_name}/{fecha}')
async def detalle_diario_ruta(company_name: str, fecha: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_detalle_diario_por_rutas(fecha))



#FTP




#cliente_nuevo

@app.get('/home_api/clientes_nuevos/{company_name}/{fecha}')
async def clientes_nuevos(company_name: str, fecha: str):
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_clientes_nuevos(fecha))

@app.get('/home_api/clientes_nuevos_ruta_fecha/{company_name}/{ruta}/{fecha}')
async def clientes_nuevos_ruta_fecha(company_name: str, ruta: str, fecha: str):
    #comp = company_single(name=company_name.upper())
    return get_defaul_xss_data(company_single(name=company_name.upper()), query_clientes_nuevos_ruta(ruta, fecha))



@app.get('/home_api/parcial_total_10_all')
async def parcial_total_10_all():
    data_ = get_defaul_xss_data(company_list_DZ(), query_status_total_parcial_10_min())
    data = custom_transform(data_)
    return data




@app.get('/home_api/sincronizo_mas_una_vez_todos')
async def sincronizo_mas_una_vez_todos():
    return get_defaul_xss_data(company_list_DZ(), query_sincronizo_mas_de_una_vez())

#DETALLE DIARIO
@app.get('/home_api/detalle_diario/{company_name}/{fecha}')
async def detalle_diario(company_name: str, fecha: str):
    data = get_defaul_xss_data(company_single(name=company_name.upper()), query_detalle_diario(fecha))
    #data = custom_transform(data_)
    return data


@app.get('/home_api/detalle_diario_todos/{fecha}')
async def detalle_diario(fecha: str):
    data_ = get_defaul_xss_data(company_list_DZ(), query_detalle_diario(fecha))
    data = custom_transform(data_)
    return data

#documentos_ventas_exceden
@app.get('/home_api/documentos_ventas_exceden/{company_name}/{fecha}/{timer}')
async def detalle_diario(company_name: str, fecha: str, timer: int):
    data_ = get_defaul_xss_data(company_single(name=company_name.upper()), documentos_ventas_tiempo_excedido(fecha, timer))
    data = custom_transform(data_)
    return data

#documentos_entregas_exceden
@app.get('/home_api/documentos_entregas_exceden/{company_name}/{fecha}/{timer}')
async def detalle_diario(company_name: str, fecha: str, timer: int):
    data_ = get_defaul_xss_data(company_single(name=company_name.upper()), documentos_entregas_tiempo_excedido(fecha, timer))
    data = custom_transform(data_)
    return data


 