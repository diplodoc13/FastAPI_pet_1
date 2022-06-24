from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import schemas, models
from blog.hashing import Hash


def create_user(db: Session, request: schemas.PDUser):
    new_user = models.SAUser(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, user_id: int):
    user = db.query(models.SAUser).filter(models.SAUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    return user
