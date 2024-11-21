from fastapi import FastAPI
from .routers import customers

app = FastAPI()
app.include_router(customers.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
