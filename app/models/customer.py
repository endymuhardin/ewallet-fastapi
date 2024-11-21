from sqlalchemy import Column, String
from app.database import Base


class Customer(Base):
    __tablename__ = "customer"

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)