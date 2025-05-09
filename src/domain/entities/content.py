from pydantic import BaseModel


class Content(BaseModel):
    id: str
    title: str
    description: str
    metadata: dict
