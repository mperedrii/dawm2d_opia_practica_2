# Predicción del precio de casas en California (servicio web)
Autores: Andrés Córdoba, Mykola Peredrii

## Contenido del repositorio
- `app.py`: servicio FastAPI.
- `entrenar_modelo.py`: script que entrena el modelo.
- `modelo_california.pkl`: modelo entrenado.
- `requirements.txt`: dependencias.
- `medir_tiempos.py`: medición de tiempos de respuesta.

## Pasos del despliegue
1. Subir el repositorio a GitHub.
2. Crear un Web Service en Render conectado al repositorio.
3. Build: `pip install -r requirements.txt`; Start: `uvicorn app:app --host 0.0.0.0 --port $PORT`.

## URL final
https://dawm2d-opia-practica-2.onrender.com
