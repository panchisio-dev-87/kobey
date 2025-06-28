# main.py
from fastapi import FastAPI
from datetime import datetime
import pytz

from core.company import company_list_grupo_1
from core.controller import get_defaul_xss_data
from core.helpers import custom_transform
from core.query import query_stock_dz

# Crea una instancia de la aplicación FastAPI
app = FastAPI()

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

@app.get('/home_api/stock_grupo_1')
async def stock_grupo_1():
    data_ = get_defaul_xss_data(company_list_grupo_1(), query_stock_dz())
    data = custom_transform(data_)
    return data