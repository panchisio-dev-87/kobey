# Dockerfile

# 1. Usa una imagen base de Python oficial y ligera.
FROM python:3.11-slim

# 2. Establece el directorio de trabajo dentro del contenedor.
WORKDIR /app

# 3. Copia el archivo de dependencias y las instala.
# Se hace en un paso separado para aprovechar el caché de Docker.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia el resto del código de tu aplicación al contenedor.
COPY . .

# 5. Comando para ejecutar la aplicación.
# Uvicorn se ejecuta en el host 0.0.0.0 para ser accesible desde fuera
# del contenedor. Koyeb mapeará automáticamente su puerto externo al puerto 8000.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]