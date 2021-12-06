from ..schemas.detalle import *
from ..config.db import *

from fastapi import Depends, APIRouter

details = APIRouter()


    # Mostrar detalle
def cargardetalle():
    detalle = []
    for Art in Factura_Detalle.select().dicts():
        detalle.append(Art)
    return detalle

@details.get("/detalle/", tags=['detalle'])
def lista_detalle():
    tmp = cargardetalle()
    return tmp


    # Actualizar detalle
def actualizardetalle(obj:factura_detalle, codigo: int):
    Art=factura_detalle.get(factura_detalle.codigo == codigo)
    Art.nombre = obj.nombre
    Art.precio = obj.precio
    Art.cantidad = obj.cantidad
    Art.total = obj.total
    Art.save()

@details.put("/detalle/{codigo}", tags=['detalle'])
def actualizar_detalle(Art: factura_detalle, codigo: int):
    actualizardetalle(Art, codigo=codigo)
    return {"Mensaje": "Se actualizo el articulo"}


    # Eliminar detalle
def eliminardetalle(codigo: int):
  Art=factura_detalle.delete().where(factura_detalle.codigo == codigo)
  Art.execute()

@details.delete("/detalle/{codigo}", tags=['detalle'])
def eliminar_detalle(codigo: int):
    eliminardetalle(codigo)
    return {"Mensaje": "Se elimino el articulo"}

