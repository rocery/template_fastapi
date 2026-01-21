from fastapi import FastAPI
from app.config import get_settings
from app.routers import user, device

app = FastAPI()

app.include_router(user.router)
app.include_router(device.router)

@app.get("/")
async def read_root():
    settings = get_settings()
    return {"app_name": settings.APP_NAME, "version": settings.APP_VERSION}
    # return {"Hello": "World"}