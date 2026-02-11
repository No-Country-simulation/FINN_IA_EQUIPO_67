from fastapi import FastAPI
from app.routers import health, users, parse, transactions, categories, apps, stats, settings, sync
from app.database import init_db

app = FastAPI(title="Finn Backend")

# incluir routers
app.include_router(health.router)
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(parse.router, prefix="/api/v1/parse", tags=["parse"])
app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["transactions"])
app.include_router(categories.router, prefix="/api/v1/categories", tags=["categories"])
app.include_router(apps.router, prefix="/api/v1/apps", tags=["apps"])
app.include_router(stats.router, prefix="/api/v1/stats", tags=["stats"])
app.include_router(settings.router, prefix="/api/v1/settings", tags=["settings"])
app.include_router(sync.router, prefix="/api/v1/sync", tags=["sync"])

@app.on_event("startup")
async def on_startup():
    # inicializa conexión a la base de datos (si aplica)
    await init_db()
