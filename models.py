from sqlalchemy import Column, Integer, String
from database import Base

# Define ContactInfo class inheriting from Base
class ContactInfo(Base):
    __tablename__ = 'details'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    phone = Column(Integer)