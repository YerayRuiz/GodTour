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

def find_usuario_by_email(email):
    usuario = usuario_db.find_one({ 'correo': { "$regex": email + '.*', "$options" :'i' }})
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

def update_usuario(id, nombre_completo, correo, dni, fecha_nacimiento, antiguedad_permiso, foto_perfil, valoracion_media):
    filter = {"_id": ObjectId(id)}
    new_values = {"$set":{
        "nombre_completo": nombre_completo,
        "correo": correo,
        "dni": dni,
        "fecha_nacimiento": fecha_nacimiento,
        "antiguedad_permiso": antiguedad_permiso,
        "foto_perfil": foto_perfil,
        "valoracion_media": valoracion_media
    }}
        
    result = usuario_db.update_one(filter, new_values)
    if result.matched_count == 0:
        return "Fallo"
    else:
        return "Acierto"

def delete_usuario(id):
    usuario_db.delete_one({'_id': ObjectId(id)})