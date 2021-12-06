from ..schemas.clientes import *
from ..config.db import *

from fastapi import APIRouter

customers = APIRouter()


    # Mostrar Clientes
def cargarClientes():
    clientes = []
    for client in Clientes.select().dicts():
        clientes.append(client)
    return clientes

@customers.get("/clientes/", tags=['Clientes'])
def lista_Clientes():
    tmp = cargarClientes()
    return tmp


    # Crear Cliente
def guardarCliente(obj:clientes):
        client = Clientes()
        client.cedula = obj.cedula
        client.nombre = obj.nombre
        client.apellido = obj.apellido
        client.correo = obj.correo
        client.rnc = obj.rnc
        client.telefono = obj.telefono
        client.save()  

@customers.post("/clientes/", tags=['Clientes'])
def agregar_Cliente(client: clientes):
    guardarCliente(client)
    return {"Mensaje": "Se guardo el cliente"}


    # Actualizar Cliente
def actualizarCliente(obj:clientes, cedula: int):
    client=Clientes.get(Clientes.cedula == cedula)
    client.nombre = obj.nombre
    client.apellido = obj.apellido
    client.correo = obj.correo
    client.rnc = obj.rnc
    client.telefono = obj.telefono
    client.save()

@customers.put("/clientes/{cedula}", tags=['Clientes'])
def actualizar_Cliente(client: clientes, cedula:int):
    actualizarCliente(client, cedula=cedula)
    return {"Mensaje": "Se actualizo el clientes"}

    
    # Eliminar Cliente
def eliminarClientes(cedula: int):
  client= Clientes.delete().where(Clientes.cedula == cedula)
  client.execute()

@customers.delete("/clientes/{cedula}", tags=['Clientes'])
def eliminar_Cliente(cedula: int):
    eliminarClientes(cedula)
    return {"Mensaje": "Se elimino el clientes"}  