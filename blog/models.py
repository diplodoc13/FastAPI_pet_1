from sqlalchemy import Integer, Column, String

from blog.database import Base


class SA_Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    body = Column(String(1000), nullable=False)