from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from blog import schemas, models
from blog.database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.PD_Blog, db: Session = Depends(get_db)):
    new_blog = models.SA_Blog(**request.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    blog = db.query(models.SA_Blog). \
        filter(models.SA_Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message": "Blog deleted"}


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.PD_Blog, db: Session = Depends(get_db)):
    blog = db.query(models.SA_Blog).\
        filter(models.SA_Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.update({**request.dict(), "id": id}, synchronize_session=False)
    db.commit()
    return {"message": "Blog updated"}


@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.SA_Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def show(id, response: Response, db: Session = Depends(get_db)):
    # blog = db.query(models.SA_Blog).get(id)   this is the same as below
    blog = db.query(models.SA_Blog).filter(models.SA_Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    return blog