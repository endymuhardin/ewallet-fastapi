from fastapi import FastAPI
from .routers import customers
from .models import customer
from .database import engine

customer.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(customers.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
