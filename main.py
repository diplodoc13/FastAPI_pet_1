from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # only return 10 blog posts
    if published:
        return {'data': f'{limit} published blogs from the blog'}
    else:
        return {'data': f'{limit} blogs from the blog'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blog'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int, limit: int = 10):
    # fetch comments for blog with id = i
    return {'data': {'blog_id': id, 'comments': ['comment1', 'comment2']}}


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title: {blog.title}'}

