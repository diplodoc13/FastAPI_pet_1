from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from blog.database import Base


class SABlog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    body = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    creator = relationship("SAUser", back_populates="blogs")


class SAUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

    blogs = relationship("SABlog", back_populates="creator")