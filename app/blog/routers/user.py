from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import schemas
from blog.database import get_db
from blog.repository import user_repo

router = APIRouter(
    tags=['Users'],
    prefix='/user'
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.PDShowUser)
def create_user(request: schemas.PDUser, db: Session = Depends(get_db)):
    return user_repo.create_user(db, request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.PDShowUser)
def show_user(user_id: int, db: Session = Depends(get_db)):
    return user_repo.get_user(db, user_id)
