from typing import Optional

from pydantic import BaseModel


class PDUser(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class PDBlogBase(BaseModel):
    title: str
    body: str


class PDBlog(PDBlogBase):
    class Config:
        orm_mode = True


class PDShowUser(BaseModel):
    name: str
    email: str
    blogs: list[PDBlog] = []

    class Config:
        orm_mode = True


class PDShowBlog(BaseModel):
    title: str
    body: str
    creator: PDShowUser

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    email: Optional[str] = None

    class Config:
        orm_mode = True
