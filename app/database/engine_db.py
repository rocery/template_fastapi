from sqlalchemy import create_engine, text
from ..config import get_settings

# Database URL
DATABASE_URL_iot = get_settings().DATABASE_URL_iot

# Create engine
engine_db_iot = create_engine(
    DATABASE_URL_iot,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False,  # set True for SQL debug
)
