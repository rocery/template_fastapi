from sqlalchemy import text
from .engine_db import engine_db_iot

sql = text("""
    SELECT device_id, device_name, temperature 
    FROM suhu_ruang.device 
    ORDER BY device_id ASC 
""")

def get_devices():
    with engine_db_iot.connect() as conn:
        return conn.execute(sql).mappings().all()