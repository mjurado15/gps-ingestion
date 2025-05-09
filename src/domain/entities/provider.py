from pydantic import BaseModel


class Provider(BaseModel):
    name: str  # identificador del proveedor
    is_active: bool
    # parametria: ...
