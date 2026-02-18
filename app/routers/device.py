from fastapi import APIRouter
from fastapi.concurrency import run_in_threadpool
from ..database.list_device_sensor_suhu_ruang import get_devices
from ..database.list_data_sensor import get_data

router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)

@router.get("/")
async def list_devices():
    devices = await run_in_threadpool(get_devices)
    return {"devices": devices}

@router.get("/data")
async def list_data():
    data = await run_in_threadpool(get_data)
    return {"data": data}