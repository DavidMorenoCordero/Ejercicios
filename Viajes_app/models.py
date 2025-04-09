from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['viajes_db']

class Viaje:
    def __init__(self, origen, destino, fecha, precio, asientos_disponibles):
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.precio = precio
        self.asientos_disponibles = asientos_disponibles
        self.creado_en = datetime.now()
    
    def guardar(self):
        viaje_data = {
            'origen': self.origen,
            'destino': self.destino,
            'fecha': datetime.strptime(self.fecha, '%Y-%m-%d'),
            'precio': float(self.precio),
            'asientos_disponibles': int(self.asientos_disponibles),
            'creado_en': self.creado_en
        }
        return db.viajes.insert_one(viaje_data).inserted_id
    
    @staticmethod
    def obtener_todos():
        return list(db.viajes.find().sort('fecha', 1))
    
    @staticmethod
    def obtener_por_id(viaje_id):
        return db.viajes.find_one({'_id': ObjectId(viaje_id)})
    
    @staticmethod
    def eliminar(viaje_id):
        return db.viajes.delete_one({'_id': ObjectId(viaje_id)})
    
    @staticmethod
    def actualizar_asientos(viaje_id, cantidad):
        return db.viajes.update_one(
            {'_id': ObjectId(viaje_id)},
            {'$inc': {'asientos_disponibles': cantidad}}
        )

class Reservacion:
    def __init__(self, viaje_id, nombre_cliente, cantidad_pasajeros):
        self.viaje_id = viaje_id
        self.nombre_cliente = nombre_cliente
        self.cantidad_pasajeros = cantidad_pasajeros
        self.fecha_reservacion = datetime.now()
        
        # Obtener el viaje para calcular el total
        viaje = Viaje.obtener_por_id(viaje_id)
        self.total_pago = float(viaje['precio']) * int(cantidad_pasajeros)
    
    def guardar(self):
        reservacion_data = {
            'viaje_id': ObjectId(self.viaje_id),
            'nombre_cliente': self.nombre_cliente,
            'cantidad_pasajeros': int(self.cantidad_pasajeros),
            'fecha_reservacion': self.fecha_reservacion,
            'total_pago': self.total_pago
        }
        return db.reservaciones.insert_one(reservacion_data).inserted_id
    
    @staticmethod
    def obtener_todas():
        return list(db.reservaciones.find().sort('fecha_reservacion', -1))
    
    @staticmethod
    def obtener_por_id(reservacion_id):
        return db.reservaciones.find_one({'_id': ObjectId(reservacion_id)})
    
    @staticmethod
    def eliminar(reservacion_id):
        reservacion = Reservacion.obtener_por_id(reservacion_id)
        if reservacion:
            # Devolver asientos al viaje
            Viaje.actualizar_asientos(
                reservacion['viaje_id'],
                reservacion['cantidad_pasajeros']
            )
            return db.reservaciones.delete_one({'_id': ObjectId(reservacion_id)})
        return None