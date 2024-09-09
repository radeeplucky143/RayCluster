from fastapi import FastAPI
from src.api.endpoints import router

app = FastAPI(title="RayCluster", description="Cluster Automation.")
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
