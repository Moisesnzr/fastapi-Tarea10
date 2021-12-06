from peewee import *

db = SqliteDatabase('crud/db/database.db')

#tabla cliente
class Clientes(Model):
    cedula= CharField()
    nombre= CharField()
    apellido= CharField()
    correo= CharField()
    rnc= CharField()
    telefono= CharField()
    
    class Meta:
        database = db 

#tabla articulo
class Articulos(Model):
    tipo = CharField()
    nombre = CharField()
    precio = DoubleField()
    cantidad = IntegerField()
    comentario = CharField()
    
    class Meta:
        database = db 

#tabla factura
class Factura (Model):
    fecha=TextField()
    cliente_id=IntegerField()
    Descripcion = TextField()
    Subtotal=DoubleField()
    Itbis = DoubleField()
    Total = DoubleField()

    class Meta:
        database = db 
   
#tabla detalle factura

class Factura_Detalle (Model):
    factura_id = ForeignKeyField(Factura,backref='detalle')
    nombre= TextField()
    precio=DoubleField()
    cantidad=DoubleField()
    total=DoubleField()

    class Meta:
        database = db 

db.connect()
db.create_tables([Clientes,Articulos,Factura,Factura_Detalle])