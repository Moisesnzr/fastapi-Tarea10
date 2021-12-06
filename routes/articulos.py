from ..schemas.articulos import *
from ..config.db import *

from fastapi import Depends, APIRouter

articles = APIRouter()


    # Mostrar Articulos
def cargarArticulos():
    articulos = []
    for Art in Articulos.select().dicts():
        articulos.append(Art)
    return articulos

@articles.get("/articulos/", tags=['Articulos'])
def lista_Articulos():
    tmp = cargarArticulos()
    return tmp


    # Crear Articulos
def guardarArticulos(obj:articulos):
         Art = Articulos()
         Art.codigo = obj.codigo
         Art.tipo = obj.tipo
         Art.nombre = obj.nombre
         Art.precio = obj.precio
         Art.cantidad = obj.cantidad
         Art.comentario = obj.comentario
         Art.save()

@articles.post("/articulos/", tags=['Articulos'])
def agregar_Articulos(Art: articulos):
    guardarArticulos(Art)
    return {"Mensaje": "Se agrego el articulo"}


    # Actualizar Articulos
def actualizarArticulos(obj:articulos, nombre: str):
    Art=Articulos.get(Articulos.nombre == nombre)
    Art.tipo = obj.tipo
    Art.nombre = obj.nombre
    Art.precio = obj.precio
    Art.cantidad = obj.cantidad
    Art.comentario = obj.comentario
    Art.save()

@articles.put("/articulos/{nombre}", tags=['Articulos'])
def actualizar_Articulos(Art: articulos, nombre: str):
    actualizarArticulos(Art, nombre=nombre)
    return {"Mensaje": "Se actualizo el articulo"}


    # Eliminar Articulos
def eliminarArticulos(nombre: str):
  Art=Articulos.delete().where(Articulos.nombre == nombre)
  Art.execute()

@articles.delete("/articulos/{nombre}", tags=['Articulos'])
def eliminar_Articulos(nombre: str):
    eliminarArticulos(nombre)
    return {"Mensaje": "Se elimino el articulo"}

