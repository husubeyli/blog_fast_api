from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session
from fastapi.encoders import jsonable_encoder

from schemas import UserDisplay
from db.hash import Hash
from db.models import UserDb

from schemas import UserBase


def create_user(db: Session, request: UserBase):
    new_user = UserDb(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(UserDb).all()


def get_user(db: Session, user_id: int):
    user = db.query(UserDb).filter(UserDb.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {user_id} not found')
    return user


def update_user(db: Session, user_id: int, request: UserBase):
    user = db.query(UserDb).filter(UserDb.id == user_id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {user_id} not found')
    user.update({
        UserDb.username: request.username if request.username else UserDb.username,
        UserDb.email: request.email if request.email else UserDb.email,
        UserDb.password: Hash.bcrypt(
            request.password) if request.password else UserDb.password
    })
    db.commit()
    return JSONResponse(
        {
            'message': 'User successfull updated!',
            'user': jsonable_encoder(UserDisplay(
                username=user.first().username,
                email=user.first().email
            ))
        },
        status_code=200)


def delete_user(db: Session, user_id: int):
    user = db.query(UserDb).filter(UserDb.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {user_id} not found')
    db.delete(user)
    db.commit()
    return f'User with id {user_id} not found'
    # try:
    #     user = db.query(UserDb).filter(UserDb.id == user_id).first()
    #     db.delete(user)
    #     db.commit()
    #     return JSONResponse({'message': 'User successfull deleted!'}, status_code=200)
    # except:
    #     return JSONResponse({'message': 'User not founded'}, status_code=404)
