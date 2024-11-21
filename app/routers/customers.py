from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/customer",
    tags=["customers"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{customer_id}")
async def read_items():
    return {"id": "c001", "name": "Customer 001", "email" : "c001@yopmail.com"}