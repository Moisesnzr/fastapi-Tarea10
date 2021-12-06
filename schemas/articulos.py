from pydantic import BaseModel
from typing import Optional


class articulos (BaseModel):
    codigo: int
    tipo :str
    nombre : str
    precio : float
    cantidad : int
    comentario : str

    class Config:
        orm_mode = True