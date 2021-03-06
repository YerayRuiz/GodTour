from mongoDB import trayecto_db
from mongoDB import usuario_db
from mongoDB import conversacion_db
from bson import json_util
from bson.objectid import ObjectId
import fechas as date_converter
from datetime import datetime
def find_conversaciones():
    conversaciones = conversacion_db.find()
    return conversaciones

def find_conversacion(id):
    conversacion = conversacion_db.find_one({'_id': ObjectId(id)})
    return conversacion

def find_conversaciones_trayecto(id):
    conversaciones_trayecto = conversacion_db.find({'trayecto': ObjectId(id)})
    return conversaciones_trayecto

def find_conversaciones_autor(id):
    conversaciones_autor = conversacion_db.find({'autor': ObjectId(id)})
    return conversaciones_autor

def create_conversacion(trayecto, autor, texto):
    conversacion_db.insert_one(
        {
            "trayecto": ObjectId(trayecto),
            "autor": ObjectId(autor),
            "texto": str(texto),
            "stamp": datetime.now().timestamp() })

def delete_conversacion(id):
    result = conversacion_db.delete_one({'_id': ObjectId(id)})
    return result

def delete_conversacion_trayecto(id_trayecto):
    result = conversacion_db.delete_many({'trayecto': ObjectId(id_trayecto)})
    return result

###################################################################################################################################
# QUERIES
###################################################################################################################################


