from pydantic import BaseModel
from typing import Optional

class factura_detalle (BaseModel):
    codigo:int
    factura_id:int
    nombre:str
    precio:float
    cantidad:float
    total:float

    class Config:
        orm_mode = True