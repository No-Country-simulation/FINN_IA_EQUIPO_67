from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.config import settings

security = HTTPBearer()

# inicializar firebase admin cuando haya credenciales
_firebase_initialized = False

async def _init_firebase():
    global _firebase_initialized
    if _firebase_initialized:
        return
    try:
        import firebase_admin
        from firebase_admin import credentials
    except Exception:
        # firebase_admin no instalado
        return

    creds = None
    if settings.FIREBASE_CREDENTIALS:
        # ruta al archivo JSON
        creds = credentials.Certificate(settings.FIREBASE_CREDENTIALS)
    elif settings.FIREBASE_CREDENTIALS_JSON:
        import json
        creds = credentials.Certificate(json.loads(settings.FIREBASE_CREDENTIALS_JSON))

    if creds:
        try:
            firebase_admin.initialize_app(creds, {"projectId": settings.FIREBASE_PROJECT_ID})
            _firebase_initialized = True
        except Exception:
            # si ya fue inicializado o falla, ignorar
            _firebase_initialized = True


async def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if not token:
        raise HTTPException(status_code=401, detail="Token inválido")

    # intentar validar con firebase-admin
    await _init_firebase()
    try:
        import firebase_admin
        from firebase_admin import auth as firebase_auth
    except Exception:
        # firebase-admin no disponible, aceptar token mock (solo desarrollo)
        if settings.ENVIRONMENT != "production":
            return {"uid": "mock-user"}
        raise HTTPException(status_code=500, detail="Firebase Admin no configurado")

    try:
        decoded = firebase_auth.verify_id_token(token)
        return decoded
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Token inválido: {e}")
