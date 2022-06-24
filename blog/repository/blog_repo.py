from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import models, schemas


def create_blog(db: Session, user_id: int, request: schemas.PDBlog):
    new_blog = models.SABlog(**request.dict(), user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_blog(db: Session, blog_id: int):
    # blog = db.query(models.SA_Blog).get(id)   this is the same as the line below
    blog = db.query(models.SABlog).filter(models.SABlog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} not found")
    return blog


def get_all_blogs(db: Session):
    blogs = db.query(models.SABlog).all()
    return blogs


def update_blog(db: Session, blog_id: int, request: schemas.PDBlog):
    blog = db.query(models.SABlog).filter(models.SABlog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.update({**request.dict(), "id": blog_id}, synchronize_session=False)
    db.commit()
    return {"message": "Blog updated"}


def delete_blog(db: Session, blog_id: int):
    blog = db.query(models.SABlog).filter(models.SABlog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted"}
