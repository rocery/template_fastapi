from sqlalchemy import text
from .engine_db import engine_db_iot

sql = text("""
    SELECT device_id, device_name, temperature, humidity, date FROM suhu_ruang.data_suhu 
    WHERE 
    1 = 1 
    ORDER BY `date` DESC 
    LIMIT 100
""")

def get_data():
    with engine_db_iot.connect() as conn:
        return conn.execute(sql).mappings().all()