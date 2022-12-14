from fastapi import FastAPI, Depends
from .core.config import Settings
from .core.dependencies import get_settings

app = FastAPI()


@app.get("/")
def read_root(settings: Settings = Depends(get_settings)):
    """
        Health checkpoint
    """
    return {"msg": f"Hello World from {settings.ENV}"}
