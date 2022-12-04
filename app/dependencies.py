from functools import lru_cache
from . import config
from app.db import session


@lru_cache()
def get_settings():
    return config.Settings()


def get_db():
    db = session.SessionLocal()
    try:
        yield db
    finally:
        db.close()
