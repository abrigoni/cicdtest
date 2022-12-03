from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
        Health checkpoint
    """
    return {"msg": "Hello World"}
