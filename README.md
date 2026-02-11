Proyecto Finn Backend (FastAPI)

Estructura inicial creada.

Requisitos: Python 3.12

Cómo ejecutar (local):
1. Copiar `.env.example` a `.env` y ajustar variables (especialmente `DATABASE_URL` y `FIREBASE_CREDENTIALS`).
2. Crear un service account en Firebase y descargar el JSON. Colocar la ruta en `FIREBASE_CREDENTIALS`.
3. Instalar dependencias: `pip install -r requirements.txt`.
4. Ejecutar: `uvicorn app.main:app --reload --factory` o `uvicorn app.main:app --reload`.

Ejecutar con Docker:
1. `docker-compose up --build` (el servicio web usa Python 3.12 en la imagen).

Notas:
- `app/auth.py` valida tokens con `firebase-admin` si está configurado; en `development` acepta un mock.
