from fastapi import APIRouter

router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)

@router.get("/")
async def read_devices():
    return [{"device_id": "device1"}, {"device_id": "device2"}]