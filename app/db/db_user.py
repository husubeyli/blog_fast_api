from sqlalchemy.orm.session import Session
from db.hash import Hash
from db.models import UserDb

from schemas import UserBase

def create_user(db: Session, request: UserBase):
    new_user = UserDb(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
    
def get_all_users(db: Session):
    return db.query(UserDb).all()

def get_one_user(db: Session, user_id: int):
    try:
        db.query(UserDb).filter(UserDb.id == user_id).first()
    except:
        print('salam')
        return "User not found"
    return db.query(UserDb).filter(UserDb.id == user_id).first()