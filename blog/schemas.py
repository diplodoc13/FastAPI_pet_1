from pydantic import BaseModel


class PD_Blog(BaseModel):
    title: str
    body: str