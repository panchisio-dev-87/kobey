# main.py
from fastapi import FastAPI
from datetime import datetime
import pytz

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