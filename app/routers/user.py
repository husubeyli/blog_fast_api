from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import UserDisplay
from typing import List

from db.databse import get_db
from schemas import UserBase
from db import db_user


router = APIRouter(
    prefix="/users",
    tags=["user"],
)


# Create user
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# Read all user
@router.get('/', response_model=List[UserDisplay])
def get_all_user(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


# Read one user
@router.get('/{user_id}', response_model=UserDisplay)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_one_user(db, user_id)

# Update user

# Delete user
