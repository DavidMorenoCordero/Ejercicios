from pymongo import MongoClient
from datetime import datetime

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['viajes_db']

# Colecciones
viajes = db['viajes']
reservaciones = db['reservaciones']

def agregar_viaje(origen, destino, fecha, precio, asientos):
    viaje = {
        'origen': origen,
        'destino': destino,
        'fecha': datetime.strptime(fecha, '%Y-%m-%d'),
        'precio': float(precio),
        'asientos_disponibles': int(asientos),
        'creado_en': datetime.now()
    }
    return viajes.insert_one(viaje).inserted_id

def listar_viajes():
    return list(viajes.find().sort('fecha', 1))

def hacer_reservacion(viaje_id, nombre_cliente, cantidad_pasajeros):
    viaje = viajes.find_one({'_id': viaje_id})
    if viaje and viaje['asientos_disponibles'] >= cantidad_pasajeros:
        reservacion = {
            'viaje_id': viaje_id,
            'nombre_cliente': nombre_cliente,
            'cantidad_pasajeros': int(cantidad_pasajeros),
            'fecha_reservacion': datetime.now(),
            'total_pago': viaje['precio'] * cantidad_pasajeros
        }
        # Actualizar asientos disponibles
        viajes.update_one(
            {'_id': viaje_id},
            {'$inc': {'asientos_disponibles': -cantidad_pasajeros}}
        )
        return reservaciones.insert_one(reservacion).inserted_id
    return None

def listar_reservaciones():
    return list(reservaciones.find().sort('fecha_reservacion', -1))

def cancelar_reservacion(reservacion_id):
    reservacion = reservaciones.find_one({'_id': reservacion_id})
    if reservacion:
        # Devolver asientos al viaje
        viajes.update_one(
            {'_id': reservacion['viaje_id']},
            {'$inc': {'asientos_disponibles': reservacion['cantidad_pasajeros']}}
        )
        reservaciones.delete_one({'_id': reservacion_id})
        return True
    return False