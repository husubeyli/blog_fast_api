from xmlrpc.client import Boolean
from sqlalchemy import Column, Integer, String
from db.databse import Base


class UserDb(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String)
    password = Column(String)
    