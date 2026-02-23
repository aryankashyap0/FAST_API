import os
from typing import Union
from fastapi import FastAPI

app = FastAPI()
# Hello
@app.get("/")
def read_root():
    # Filter to show only your custom vars (not AWS_ prefixed)
    custom_vars = {
        key: value for key, value in os.environ.items()
        if not key.startswith(("AWS_", "LAMBDA_", "PATH", "_", "LD_", "PYTHON", "TZ", "SHLVL", "LANG", "LC_", "PWD"))
    }
    return {
        "message": "Hello World!",
        "env_vars": custom_vars,
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
