from ..schemas.facturas import *
from ..schemas.detalle import *
from ..config.db import *

from fastapi import APIRouter

invoice = APIRouter()


    # Mostrar Factura
def cargarFactura():
    factura = []
    for fac in Factura.select().dicts():
        factura.append(fac)
    return factura

@invoice.get("/factura/", tags=['Factura'])
def lista_Factura():
    tmp = cargarFactura()
    return tmp


    # Crear Factura
def guardarFactura(obj:factura):
    fac = Factura()
    fac.fecha= obj.fecha
    fac.cliente_id=obj.cliente_id
    fac.Descripcion =obj.Descripcion
    fac.Subtotal=obj.Subtotal
    fac.Itbis = obj.Itbis
    fac.Total = obj.Total
    obj.detalle
    fac.save()

    for dett in obj.detalle:
        det = Factura_Detalle()
        det.factura_id = dett.factura_id
        det.codigo = dett.codigo
        det.nombre = dett.nombre
        det.precio = dett.precio
        det.cantidad = dett.cantidad
        det.total = dett.total
        det.save()

@invoice.post("/factura/", tags=['Factura'])
def agregar_Factura(Fac: factura):
    guardarFactura(Fac)
    return {"Mensaje": "Se guardo la factura" + str(len(Fac.detalle))}


    # Actualizar Factura
def actualizarFactura(obj:factura, codigo: int):
    fac = Factura.get(Factura.id == codigo)
    fac.fecha= obj.fecha
    fac.cliente_id=obj.cliente_id
    fac.Descripcion =obj.Descripcion
    fac.Subtotal=obj.Subtotal
    fac.Itbis = obj.Itbis
    fac.Total = obj.Total
    obj.detalle
    fac.save()

    for dett in obj.detalle:
        det = Factura_Detalle()
        det.factura_id = dett.factura_id
        det.codigo = dett.codigo
        det.nombre = dett.nombre
        det.precio = dett.precio
        det.cantidad = dett.cantidad
        det.total = dett.total
        det.save()

@invoice.put("/factura/{codigo}", tags=['Factura'])
def actualizar_Factura(Fac: factura, codigo: int):
    actualizarFactura(Fac, codigo=codigo)
    return {"Mensaje": "Se actualizo la factura"}


    # Eliminar Factura
def eliminarFactura(codigo: int):
    fac=Factura.delete().where(Factura.id == codigo)
    fac.execute()

@invoice.delete("/factura/{codigo}", tags=['Factura'])
def eliminar_Factura(codigo: int):
    eliminarFactura(codigo)
    return {"Mensaje": "Se elimino la factura"}  