from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

# 1. Inicializa o aplicativo FastAPI
app = FastAPI(
    title="Railway Test API",
    description="API simples para teste de deploy e health check."
)

# 2. Configurações de CORS
origins = ["*"] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Health Check Endpoint
@app.get("/health", tags=["System"])
def health_check():
    """Retorna o status 'ok' para health checks."""
    return {"status": "ok", "environment": os.getenv("RAILWAY_ENVIRONMENT_NAME", "Local")}

# 4. Hello World Endpoint
@app.get("/", tags=["Root"])
def read_root():
    """Retorna a mensagem 'Hello world'."""
    return {"message": "Hello world from Railway Test API"}
