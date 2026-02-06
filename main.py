from fastapi import FastAPI, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.routers import user, device

app = FastAPI()

app.include_router(user.router)
app.include_router(device.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

@app.route("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/test_setting")
async def test_setting(request: Request):
    settings = get_settings()
    return {
        "app_name": settings.APP_NAME,
        "app_version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "description": settings.DESCRIPTION,
        # "db_host": settings.DATABASE_URL_iot
    }