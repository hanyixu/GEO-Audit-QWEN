from fastapi import FastAPI

from app.routes.audit import router as audit_router

app = FastAPI(
    title="GEO Audit API",
    description="FastAPI backend for GEO audit skills",
    version="1.0.0",
)

app.include_router(audit_router)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
