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
async def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# Read all user
@router.get('/all', response_model=List[UserDisplay])
async def get_all_user(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


# Read one user
@router.get('/{user_id}', response_model=UserDisplay)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, user_id)


# Update user
@router.put('/{user_id}', response_model=UserDisplay)
async def update_user(user_id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, user_id, request)

# Delete user


@router.get('/delete/{user_id}')
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, user_id)
