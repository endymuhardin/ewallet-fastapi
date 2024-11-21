from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.customer import Customer
from app.database import get_db

router = APIRouter(
    prefix="/customer",
    tags=["customers"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_all_customer(db: Session = Depends(get_db)):
    customers = db.query(Customer).all()
    return customers

@router.get("/{customer_id}")
async def get_customer_by_id(customer_id: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    return customer