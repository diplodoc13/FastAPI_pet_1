from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import schemas, oauth2
from blog.database import get_db
from blog.repository import blog_repo


router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.PDBlog)
def create(user_id: int, request: schemas.PDBlog, db: Session = Depends(get_db),
           current_user: schemas.PDUser = Depends(oauth2.get_current_user)):
    return blog_repo.create_blog(db, user_id, request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.PDShowBlog)
def show(blog_id: int, db: Session = Depends(get_db), current_user: schemas.PDUser = Depends(oauth2.get_current_user)):
    return blog_repo.get_blog(db, blog_id)


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[schemas.PDShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.PDUser = Depends(oauth2.get_current_user)):
    return blog_repo.get_all_blogs(db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(blog_id: int, request: schemas.PDBlog, db: Session = Depends(get_db),
           current_user: schemas.PDUser = Depends(oauth2.get_current_user)):
    return blog_repo.update_blog(db, blog_id, request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(blog_id: int, db: Session = Depends(get_db),
            current_user: schemas.PDUser = Depends(oauth2.get_current_user)):
    return blog_repo.delete_blog(db, blog_id)
