from mongoDB import usuario_db
from bson import json_util
from bson.objectid import ObjectId
from datetime import datetime
def find_usuarios():
    usuarios = usuario_db.find()
    return usuarios

def find_usuario(id):
    usuario = usuario_db.find_one({'_id': ObjectId(id)})
    return usuario

def create_usuario(nombre_completo,correo,dni,fecha_nacimiento,antiguedad_permiso,
foto_perfil,valoracion_media):
        id = usuario_db.insert_one(
            {
             "nombre_completo": nombre_completo,
             "correo": correo,
             "dni": dni,
             "fecha_nacimiento": fecha_nacimiento,
             "antiguedad_permiso": antiguedad_permiso,
             "foto_perfil": foto_perfil,
             "valoracion_media": valoracion_media
            }
        )
