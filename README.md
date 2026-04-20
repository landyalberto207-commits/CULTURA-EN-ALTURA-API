# CULTURA-EN-ALTURA-API

API REST construida con FastAPI para Cultura en Altura.

## Ejecutar localmente

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

La documentación queda disponible en /docs y el health check en /health.

## Despliegue en Render

Este repositorio ya incluye un blueprint en [render.yaml](render.yaml) para desplegar el backend como Web Service.

Configuración usada por Render:

- Root Directory: backend
- Build Command: pip install -r requirements.txt
- Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
- Health Check Path: /health

Variables de entorno requeridas en Render:

- SUPABASE_URL
- SUPABASE_SERVICE_KEY
- CORS_ALLOWED_ORIGINS

Ejemplo de CORS_ALLOWED_ORIGINS:

- https://tu-frontend.onrender.com
- https://tu-frontend.onrender.com,http://localhost:3000

Pasos:

1. Sube este repositorio a GitHub.
2. En Render, crea un nuevo Blueprint o Web Service apuntando al repositorio.
3. Define SUPABASE_URL, SUPABASE_SERVICE_KEY y CORS_ALLOWED_ORIGINS en el panel de variables de entorno.
4. Despliega y verifica que /health responda 200.

Nota: el archivo backend/.env sirve para desarrollo local. En Render debes usar variables de entorno del servicio, no depender del archivo .env. Para producción, evita usar CORS abierto y registra la URL real del frontend en CORS_ALLOWED_ORIGINS.