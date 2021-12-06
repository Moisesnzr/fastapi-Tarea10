from pydantic import BaseModel
from typing import Optional

class clientes(BaseModel):
    id:int
    cedula:int
    nombre:str
    apellido:str
    correo:str
    rnc:str
    telefono:str

    class Config:
        orm_mode = True