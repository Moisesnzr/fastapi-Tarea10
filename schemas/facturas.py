from pydantic import BaseModel
from typing import Optional, List
from .detalle import factura_detalle

class factura (BaseModel):
    id:int
    fecha: str
    cliente_id:int
    Descripcion:str
    Subtotal:float
    Itbis:float
    Total:float
    detalle:List[factura_detalle] = []

    class Config:
        orm_mode = True